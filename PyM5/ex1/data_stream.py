from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0
        self.error_count: int = 0
        self.batch_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return [item for item in data_batch if item is not None]
        return [
            item for item in data_batch
            if item is not None and criteria.lower() in str(item).lower()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
            "error_count": self.error_count,
            "batch_count": self.batch_count,
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Environmental Data"
        self.temperature_readings: List[float] = []

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            readings = self.filter_data(data_batch)
            temps: List[float] = []

            for item in readings:
                if isinstance(item, dict) and "temp" in item:
                    temps.append(float(item["temp"]))
                elif isinstance(item, str) and item.startswith("temp:"):
                    temps.append(float(item.split(":")[1]))

            self.temperature_readings.extend(temps)
            self.processed_count += len(readings)
            self.batch_count += 1

            avg_temp = sum(temps) / len(temps) if temps else 0.0
            return (
                f"Sensor analysis: {len(readings)} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )
        except (ValueError, ZeroDivisionError) as e:
            self.error_count += 1
            return f"Sensor batch error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            filtered: List[Any] = []
            for item in data_batch:
                if item is None:
                    continue
                if isinstance(item, dict):
                    temp = item.get("temp", 0)
                    if float(temp) > 30 or item.get("alert"):
                        filtered.append(item)
                elif isinstance(item, str) and item.startswith("temp:"):
                    try:
                        if float(item.split(":")[1]) > 30:
                            filtered.append(item)
                    except ValueError:
                        pass
            return filtered
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        avg = (
            sum(self.temperature_readings) / len(self.temperature_readings)
            if self.temperature_readings
            else 0.0
        )
        stats.update({
            "stream_type": self.stream_type,
            "avg_temperature": round(avg, 2),
            "total_temp_readings": len(self.temperature_readings),
        })
        return stats


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "Financial Data"
        self.net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            operations = self.filter_data(data_batch)
            net: float = 0.0

            for item in operations:
                if isinstance(item, dict):
                    if item.get("type") == "buy":
                        net += float(item.get("amount", 0))
                    elif item.get("type") == "sell":
                        net -= float(item.get("amount", 0))
                elif isinstance(item, str):
                    parts = item.split(":")
                    if len(parts) == 2:
                        op, value = parts[0], float(parts[1])
                        net += value if op == "buy" else -value

            self.net_flow += net
            self.processed_count += len(operations)
            self.batch_count += 1

            sign = "+" if net >= 0 else ""
            return (
                f"Transaction analysis: {len(operations)} operations, "
                f"net flow: {sign}{net:.0f} units"
            )
        except (ValueError, IndexError) as e:
            self.error_count += 1
            return f"Transaction batch error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            filtered: List[Any] = []
            for item in data_batch:
                if item is None:
                    continue
                try:
                    if isinstance(item, dict):
                        if float(item.get("amount", 0)) > 100:
                            filtered.append(item)
                    elif isinstance(item, str) and ":" in item:
                        if float(item.split(":")[1]) > 100:
                            filtered.append(item)
                except ValueError:
                    pass
            return filtered
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({
            "stream_type": self.stream_type,
            "net_flow": round(self.net_flow, 2),
        })
        return stats


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type: str = "System Events"
        self.error_events: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events = self.filter_data(data_batch)
            errors = sum(
                1 for e in events
                if (isinstance(e, str) and "error" in e.lower())
                or (isinstance(e, dict) and e.get("level") == "error")
            )
            self.error_events += errors
            self.processed_count += len(events)
            self.batch_count += 1

            return (
                f"Event analysis: {len(events)} events, "
                f"{errors} error{'s' if errors != 1 else ''} detected"
            )
        except Exception as e:
            self.error_count += 1
            return f"Event batch error: {e}"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "error":
            return [
                item for item in data_batch
                if item is not None and (
                    (isinstance(item, str) and "error" in item.lower())
                    or (isinstance(item, dict)
                        and item.get("level") == "error")
                )
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({
            "stream_type": self.stream_type,
            "error_events": self.error_events,
        })
        return stats


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if not isinstance(stream, DataStream):
            raise TypeError(f"Expected a DataStream,"
                            f" got {type(stream).__name__}")
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> Dict[str, str]:
        results: Dict[str, str] = {}
        for stream in self.streams:
            batch = batches.get(stream.stream_id, [])
            try:
                results[stream.stream_id] = stream.process_batch(batch)
            except Exception as e:
                results[stream.stream_id] = f"Processing failed: {e}"
        return results

    def filter_all(
        self, batches: Dict[str, List[Any]], criteria: Optional[str] = None
    ) -> Dict[str, List[Any]]:
        return {
            stream.stream_id: stream.filter_data(
                batches.get(stream.stream_id, []), criteria
            )
            for stream in self.streams
        }

    def get_all_stats(self) -> Dict[str, Dict[str, Union[str, int, float]]]:
        return {stream.stream_id: stream.get_stats()
                for stream in self.streams}


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch_1 = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch_1}")
    print(sensor.process_batch(sensor_batch_1))

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id},"
          f"Type: {transaction.stream_type}")
    trans_batch_1 = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_batch_1}")
    print(transaction.process_batch(trans_batch_1))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch_1 = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch_1}")
    print(event.process_batch(event_batch_1))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_001"))
    processor.add_stream(TransactionStream("TRANS_001"))
    processor.add_stream(EventStream("EVENT_001"))

    batch_2: Dict[str, List[Any]] = {
        "SENSOR_001": ["temp:19.0", "temp:35.2"],
        "TRANS_001": ["buy:200", "sell:80", "buy:50", "sell:120"],
        "EVENT_001": ["startup", "login", "error"],
    }
    results = processor.process_all(batch_2)
    print("Batch 1 Results:")
    for stream_id, result in results.items():
        label = stream_id.split("_")[0].capitalize()
        parts = result.split(":")
        detail = parts[1].strip() if len(parts) > 1 else result
        print(f"  - {label} data: {detail}")
    print("\nStream filtering active: High-priority data only")
    filter_batches: Dict[str, List[Any]] = {
        "SENSOR_001": ["temp:28.0", "temp:38.5", "temp:22.0", "temp:41.0"],
        "TRANS_001": ["buy:50", "sell:150", "buy:10"],
        "EVENT_001": ["login", "error", "logout", "error"],
    }

    critical_sensors = processor.streams[0].filter_data(
        filter_batches["SENSOR_001"], "critical"
    )
    large_transactions = processor.streams[1].filter_data(
        filter_batches["TRANS_001"], "large"
    )

    print(
        f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
        f"{len(large_transactions)} "
        f"large transaction{'s' if len(large_transactions) != 1 else ''}"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
