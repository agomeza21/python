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
        first = self._storage.pop(0)
        self.rank += 1
        return (self.rank, first)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

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
            raise ValueError("Got exception: Improper numeric data")
        if not isinstance(data, list):
            self._storage.append(str(data))
        if isinstance(data, list):
            for element in data:
                self._storage.append(str(element))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: str | List[str]) -> None:
        pass


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        pass

    def ingest(self, data: Dict[str, str] | List[Dict[str, str]]) -> None:
        pass


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
        print(f" {e}")
    num_p.ingest([1, 2, 3, 4, 5])
    print(f"Processing data: {num_p._storage}")
    print("Extracting 3 values...")
    for i in range(0, 3):
        rank, first = num_p.output()
        print(f"Numeric value {rank}: {first}")
