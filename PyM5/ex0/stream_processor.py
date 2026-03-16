from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                return False
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")
        total = sum(data)
        avg = total / len(data)
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")
        chars = len(data)
        words = len(data.split())
        return f"Processed text: {chars} characters, {words} words"

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        known_levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
        return any(data.startswith(level) for level in known_levels)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")
        level, _, message = data.partition(": ")
        return (f"[{level if level == 'ERROR' else 'INFO'}]"
                f" {level} level detected: {message}")

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric = NumericProcessor()
    data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    if numeric.validate(data):
        print("Validation: Numeric data verified")
    result = numeric.process(data)
    print(f"Output: {numeric.format_output(result)}")
    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    text: str = "Hello Nexus World"
    print(f'Processing data: "{text}"')
    if text_proc.validate(text):
        print("Validation: Text data verified")
    result = text_proc.process(text)
    print(f"Output: {text_proc.format_output(result)}")

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    log: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log}"')
    if log_proc.validate(log):
        print("Validation: Log entry verified")
    result = log_proc.process(log)
    print(f"Output: {log_proc.format_output(result)}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    datasets: List[Any] = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready",
    ]

    for i, (processor, data) in enumerate(zip(processors, datasets), 1):
        try:
            result = processor.process(data)
            print(f"Result {i}: {processor.format_output(result)}")
        except ValueError as e:
            print(f"Result {i}: Error - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
