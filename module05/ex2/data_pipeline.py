from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self.rank: int = 0
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")
        value = self._storage.pop(0)
        current_rank = self.rank
        self.rank += 1
        return (current_rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | List[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for element in data:
                self._storage.append(str(element))
                self._total += 1
        else:
            self._storage.append(str(data))
            self._total += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        return False

    def ingest(self, data: str | List[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for element in data:
                self._storage.append(element)
                self._total += 1
        else:
            self._storage.append(data)
            self._total += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    return False
                for key, value in element.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: Dict[str, str] | List[Dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for element in data:
                if "log_level" not in element or "log_message" not in element:
                    raise ValueError("Improper log data")
                log_level = element["log_level"]
                log_message = element["log_message"]
                self._storage.append(f"{log_level}: {log_message}")
                self._total += 1
        else:
            if "log_level" not in data or "log_message" not in data:
                raise ValueError("Improper log data")
            log_level = data["log_level"]
            log_message = data["log_message"]
            self._storage.append(f"{log_level}: {log_message}")
            self._total += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_parts = []
        for rank, value in data:
            csv_parts.append(value)
        print("CSV Output:")
        print(",".join(csv_parts))


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_parts = []
        for rank, value in data:
            key = f"item_{rank}"
            json_parts.append(f'"{key}": "{value}"')
        json_str = "{" + ", ".join(json_parts) + "}"
        print("JSON Output:")
        print(json_str)


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't process element "
                      f"in stream: {element}")

    def print_processors_stats(self) -> None:
        names = {
            "NumericProcessor": "Numeric Processor",
            "TextProcessor": "Text Processor",
            "LogProcessor": "Log Processor"
        }
        if not self._processors:
            print("No processor found, no data")
        for processor in self._processors:
            name = names[type(processor).__name__]
            total = processor._total
            remaining = len(processor._storage)
            print(f"{name}: total {total} items processed, remaining "
                  f"{remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            out_list = []
            count = min(nb, len(processor._storage))
            for i in range(count):
                out_list.append(processor.output())
            plugin.process_output(out_list)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    print("")
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("")
    num_p = NumericProcessor()
    text_p = TextProcessor()
    log_p = LogProcessor()
    csv_plugin = CSVExport()
    json_plugin = JSONExport()
    print("Registering Processors")
    data_stream.register_processor(num_p)
    data_stream.register_processor(text_p)
    data_stream.register_processor(log_p)
    print("")
    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"}
        ],
        42,
        ["Hi", "five"]
    ]
    print(f"Send first batch of data on stream: {batch1}")
    print("")
    data_stream.process_stream(batch1)
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("")
    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, csv_plugin)
    print("")
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("")
    batch2 = [
        21,
        [
            'I love AI',
            'LLMs are wonderful',
            'Stay healthy'
        ],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"Send another batch of data: {batch2}")
    print("")
    data_stream.process_stream(batch2)
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
    print("")
    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, json_plugin)
    print("")
    print("== DataStream statistics ==")
    data_stream.print_processors_stats()
