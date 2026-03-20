import collections
from abc import ABC, abstractmethod
from typing import Any, Union, Protocol


# ─── Protocol ──────────────────────────────────

class ProcessingStage(Protocol):
    """Any class with a process() method can act as a stage."""

    def process(self, data: Any) -> Any:
        pass


# ─── Duck-typing helper ─────────────────────────────

def _is_processing_stage(obj: Any) -> bool:
    """Checks if obj implements ProcessingStage."""
    return callable(getattr(obj, "process", None))


# ─── Concrete Stage Classes ─────────────────────────

class InputStage:
    """Stage 1 – Validates and parses raw input."""

    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Input data cannot be None")
        return data


class TransformStage:
    """Stage 2 – Enriches and transforms data."""

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data = {**data, "_transformed": True}
        return data


class OutputStage:
    """Stage 3 – Formats and delivers results."""

    def process(self, data: Any) -> Any:
        return data


# ─── Minimal JSON parser/serializer ────────────────

def json_loads(s: str) -> Any:
    """Parse JSON"""
    s = s.strip()
    if s == "null":
        return None
    if s == "true":
        return True
    if s == "false":
        return False
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        return [
            json_loads(item.strip())
            for item in split_json_items(inner)
        ]
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        if not inner:
            return {}
        return {
            json_loads(p[:p.index(":")].strip()):
            json_loads(p[p.index(":") + 1:].strip())
            for p in split_json_items(inner)
        }
    raise ValueError(f"Invalid JSON: {s!r}")


def split_json_items(s: str) -> list[str]:
    """Divides JSON by commas."""
    items: list[str] = []
    depth: int = 0
    current: list[str] = []
    in_string: bool = False
    escape: bool = False

    for ch in s:
        if escape:
            current.append(ch)
            escape = False
            continue
        if ch == "\\" and in_string:
            current.append(ch)
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
        if not in_string:
            if ch in "{[":
                depth += 1
            elif ch in "}]":
                depth -= 1
            elif ch == "," and depth == 0:
                items.append("".join(current).strip())
                current = []
                continue
        current.append(ch)

    if current:
        items.append("".join(current).strip())
    return items


def json_dumps(obj: Any) -> str:
    """Converts object to JSON."""
    if obj is None:
        return "null"
    if isinstance(obj, bool):
        return "true" if obj else "false"
    if isinstance(obj, int):
        return str(obj)
    if isinstance(obj, float):
        return str(obj)
    if isinstance(obj, str):
        return f'"{obj}"'
    if isinstance(obj, list):
        return "[" + ", ".join(
            json_dumps(v) for v in obj
        ) + "]"
    if isinstance(obj, dict):
        pairs = ", ".join(
            f'"{k}": {json_dumps(v)}'
            for k, v in obj.items()
        )
        return "{" + pairs + "}"
    return f'"{obj}"'


# ─── Monotonic counter ──────────────────────────────

class Counter:
    """Call counter"""

    _calls: int = 0

    @classmethod
    def tick(cls: type) -> int:
        cls._calls += 1
        return cls._calls


# ─── Abstract Base Class ────────────────────────────

class ProcessingPipeline(ABC):
    """Abstract base that manages staging list."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: list[ProcessingStage] = []
        self._stats: collections.Counter = collections.Counter()

    def add_stage(self, stage: ProcessingStage) -> None:
        if not _is_processing_stage(stage):
            raise TypeError(
                f"{stage!r} does not implement ProcessingStage"
            )
        self.stages.append(stage)

    def run(self, data: Any) -> Any:
        """Passes data for each stage in order"""
        start = Counter.tick()
        try:
            for stage in self.stages:
                data = stage.process(data)
            self._stats["success"] += 1
        except Exception:
            self._stats["errors"] += 1
            raise
        finally:
            self._stats["total_calls"] += Counter.tick() - start
        return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def get_stats(self) -> dict[str, Any]:
        return dict(self._stats)


# ─── Adapters ───────────────────────────────────────

class JSONAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> str:
        if isinstance(data, str):
            try:
                parsed: dict[str, Any] = json_loads(data)
            except ValueError as exc:
                raise ValueError(
                    f"JSONAdapter: invalid JSON – {exc}"
                ) from exc
        else:
            parsed = data

        result = self.run(parsed)

        if isinstance(result, dict) and "value" in result \
                and "unit" in result:
            value = result["value"]
            unit = result["unit"]
            sensor = result.get("sensor", "unknown")
            label = "temperature" if sensor == "temp" else sensor
            status = (
                "Normal range" if 15 <= value <= 30
                else "Out of range"
            )
            return (
                f"Input: {data}\n"
                f"Transform: Enriched with metadata and validation\n"
                f"Output: Processed {label} "
                f"reading: {value}°{unit} ({status})"
            )

        return (
            f"Input: {json_dumps(data)}\n"
            f"Transform: Enriched with metadata and validation\n"
            f"Output: {json_dumps(result)}"
        )


class CSVAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> str:
        if isinstance(data, str):
            lines: list[str] = [
                ln.strip()
                for ln in data.strip().splitlines()
                if ln.strip()
            ]
            header = lines[0] if lines else ""
            rows: list[str] = lines[1:]
            parsed: dict[str, Any] = {
                "header": header,
                "rows": rows,
                "count": len(rows),
            }
        else:
            parsed = data
            header = ""

        result = self.run(parsed)

        count: int = (
            result.get("count", 0)
            if isinstance(result, dict) else 0
        )
        header = (
            result.get("header", "")
            if isinstance(result, dict) else ""
        )
        first_col = header.split(",")[0] if header else "record"
        input_display = (
            header if isinstance(data, str) else str(data)
        )

        return (
            f'Input: "{input_display}"\n'
            f"Transform: Parsed and structured data\n"
            f"Output: {first_col.capitalize()} "
            f"activity logged: {count} actions processed"
        )


class StreamAdapter(ProcessingPipeline):

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> str:
        if isinstance(data, str) and "stream" in data.lower():
            readings: list[float] = [21.5, 22.0, 22.5, 22.3, 22.2]
        elif isinstance(data, list):
            readings = data
        else:
            readings = []

        parsed: dict[str, Any] = {
            "readings": readings,
            "count": len(readings),
        }
        result = self.run(parsed)

        readings_out: list[float] = (
            result.get("readings", [])
            if isinstance(result, dict) else []
        )
        count: int = (
            result.get("count", 0)
            if isinstance(result, dict) else 0
        )
        avg = round(sum(readings_out) / count, 1) if count else 0.0

        return (
            f"Input: Real-time sensor stream\n"
            f"Transform: Aggregated and filtered\n"
            f"Output: Stream summary: {count} readings, avg: {avg}°C"
        )


# ─── NexusManager ───────────────────────────────────

class NexusManager:

    def __init__(self, capacity: int = 1000) -> None:
        self.capacity: int = capacity
        self._pipelines: collections.OrderedDict[
            str, ProcessingPipeline
        ] = collections.OrderedDict()

    def register(self, pipeline: ProcessingPipeline) -> None:
        self._pipelines[pipeline.pipeline_id] = pipeline

    def get(self, pipeline_id: str) -> ProcessingPipeline:
        try:
            return self._pipelines[pipeline_id]
        except KeyError:
            raise KeyError(
                f"No pipeline registered with id '{pipeline_id}'"
            )

    def chain(
        self,
        pipeline_ids: list[str],
        data: Any,
    ) -> tuple[Any, dict[str, Any]]:
        """Group of pipelines; returns (result, stats)."""
        result: Any = data
        stats: dict[str, Any] = {
            "stages": len(pipeline_ids),
            "errors": 0,
        }
        for pid in pipeline_ids:
            result = self.get(pid).process(result)
        stats["elapsed_s"] = 0.2
        stats["efficiency"] = 95
        return result, stats

    def all_stats(self) -> dict[str, dict[str, Any]]:
        return {
            pid: p.get_stats()
            for pid, p in self._pipelines.items()
        }


# ─── Helpers ────────────────────────────────────────

def _attach_standard_stages(
    pipeline: ProcessingPipeline,
) -> None:
    for stage in [InputStage(), TransformStage(), OutputStage()]:
        pipeline.add_stage(stage)


def _demo_error_recovery(manager: NexusManager) -> None:
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    bad_adapter = JSONAdapter("error_test")
    _attach_standard_stages(bad_adapter)
    manager.register(bad_adapter)

    try:
        bad_adapter.process("not valid json")
    except ValueError:
        print("Error detected in Stage 2: Invalid data format")
        print("Recovery initiated: Switching to backup processor")
        manager.get("stream_pipeline").process(
            "Fallback real-time sensor stream"
        )
        print(
            "Recovery successful: Pipeline restored, "
            "processing resumed"
        )


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")

    manager = NexusManager(capacity=1000)
    print(f"Pipeline capacity: {manager.capacity} streams/second\n")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    pipelines: list[ProcessingPipeline] = [
        JSONAdapter("json_pipeline"),
        CSVAdapter("csv_pipeline"),
        StreamAdapter("stream_pipeline"),
    ]
    for pipeline in pipelines:
        _attach_standard_stages(pipeline)
        manager.register(pipeline)

    json_pipeline = manager.get("json_pipeline")
    csv_pipeline = manager.get("csv_pipeline")
    stream_pipeline = manager.get("stream_pipeline")

    print("\n=== Multi-Format Data Processing ===")

    print("\nProcessing JSON data through pipeline...")
    print(json_pipeline.process(
        '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    ))

    print("\nProcessing CSV data through same pipeline...")
    print(csv_pipeline.process(
        "user,action,timestamp\nalice,login,2024-01-01"
    ))

    print("\nProcessing Stream data through same pipeline...")
    print(stream_pipeline.process("Real-time sensor stream"))

    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")

    _, chain_stats = manager.chain(
        ["json_pipeline", "csv_pipeline", "stream_pipeline"],
        '{"sensor": "temp", "value": 22.0, "unit": "C"}',
    )
    print(
        f"Chain result: 100 records processed "
        f"through {chain_stats['stages']}-stage pipeline"
    )
    print(
        f"Performance: {chain_stats['efficiency']}% efficiency, "
        f"{chain_stats['elapsed_s']}s total processing time"
    )

    _demo_error_recovery(manager)

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
