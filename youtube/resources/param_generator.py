from abc import ABC, abstractmethod
from typing import Any

class ParamGenerator(ABC):
    @abstractmethod
    def __call__(self) -> dict[str, str]:
        pass      
    
    