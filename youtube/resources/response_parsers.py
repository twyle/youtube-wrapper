from abc import ABC, abstractmethod

class ResponseParser(ABC):
    @abstractmethod
    def __call__(self, response: dict[str, str]) -> dict[str, str]:
        pass      
    
    