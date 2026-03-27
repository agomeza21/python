from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, List):
            for element in data:
                if not isinstance(element, (int, float)):
                    return False
            return True
        else:
            return False

    def process(self, data: Any) -> str:
        count = 0
        for element in data:
            count = count + 1
        sum = 0
        for element in data:
            sum = sum + element
        average = sum / count
        print(f"Output: Processed {count} numeric values, "
              f"sum={sum}, avg={average}")
