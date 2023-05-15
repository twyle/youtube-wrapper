from abc import ABC, abstractmethod
from typing import Generic, Generator, Callable, TypeVar

T = TypeVar('T')

class Resource(ABC, Generic[T]):
    @abstractmethod
    def search(self, params_generator: Callable[..., dict]) -> Generator:
        raise NotImplementedError()
    
    @abstractmethod
    def find(self, resource_id: str) -> T:
        raise NotImplementedError()
    
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError()
    
    @abstractmethod
    def __next__(self) -> list[T]:
        raise NotImplementedError()
