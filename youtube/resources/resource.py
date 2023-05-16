from abc import ABC, abstractmethod
from typing import Generic, Iterator, Callable, TypeVar

T = TypeVar('T')

class Resource(ABC, Generic[T]):
    @abstractmethod
    def search(self, params_generator: Callable[..., dict], 
               resource_id_parser: Callable[[dict[str, str]], str]) -> Iterator:
        raise NotImplementedError()
    
    @abstractmethod
    def find(self, params_generator: Callable[..., dict], resource_id: str) -> T:
        raise NotImplementedError()
    
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError()
    
    @abstractmethod
    def __next__(self) -> list[T]:
        raise NotImplementedError()
