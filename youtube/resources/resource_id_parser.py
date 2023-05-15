from abc import ABC, abstractmethod

class ResourceIdParse(ABC):
    @abstractmethod
    def __call__(self) -> str:
        pass      
    
    