from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self.rank = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        value = self._storage.pop(0)
        self.rank += 1
        return (self.rank, value)


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
        else:
            self._storage.append(str(data))


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
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(key, str) & isinstance(value, str):
                    return True
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    return False
                if isinstance(element, dict):
                    for key, value in element.items():
                        if isinstance(key, str) & isinstance(value, str):
                            return True
        return False

    def ingest(self, data: Dict[str, str] | List[Dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for element in data:
                log_level = element["log_level"]
                log_message = element["log_message"]
                self._storage.append(f"{log_level}: {log_message}")
        else:
            log_level = element["log_level"]
            log_message = element["log_message"]
            self._storage.append(f"{log_level}: {log_message}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print("")

    num_p = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': {num_p.validate(42)}")
    print(f" Trying to validate input 'Hello': "
          f"{num_p.validate("Hello")}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_p.ingest("foo")
    except ValueError as e:
        print(f" Got exception: {e}")
    data_num = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num_p.ingest(data_num)
    print(" Extracting 3 values...")
    for i in range(0, 3):
        rank, value = num_p.output()
        print(f" Numeric value {rank}: {value}")
    print("")

    text_p = TextProcessor()
    print("Testing Text Processor...")
    print(f" Trying to validate input '42': {text_p.validate(42)}")
    print(f" Trying to validate input 'Hello': {text_p.validate("Hello")}")
    print(" Test invalid ingestion of number '42' without prior validation:")
    try:
        text_p.ingest(42)
    except ValueError as e:
        print(f" Got exception: {e}")
    data_text = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data_text}")
    text_p.ingest(data_text)
    print(" Extracting 1 value...")
    rank, value = text_p.output()
    print(f" Text value {rank}: {value}")
    print("")

    log_p = LogProcessor()
    print("Testing Log Processor...")
    print(f" Trying to validate input 'Hello': {log_p.validate("Hello")}")
    print(f" Trying to validate input 'Hello: world': "
          f"{log_p.validate({"Hello": "world"})}")
    print(" Test invalid ingestion of number '42' without prior validation:")
    try:
        log_p.ingest(42)
    except ValueError as e:
        print(f" Got exception: {e}")
    data_log = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {data_log}")
    log_p.ingest(data_log)
    print(" Extracting 2 values...")
    for i in range(0, 2):
        rank, value = log_p.output()
        print(f" Log entry {rank}: {value}")
