from abc import ABC, abstractmethod
from typing import Generic, Iterator, TypeVar
from .factories import SearchFactory, FindFactory


T = TypeVar('T')

class Resource(ABC, Generic[T]):
    @abstractmethod
    def search(self, search_factory: SearchFactory) -> Iterator:
        raise NotImplementedError()
    
    @abstractmethod
    def find(self, find_factory: FindFactory, resource_id: str) -> T:
        raise NotImplementedError()
    
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError()
    
    @abstractmethod
    def __next__(self) -> list[T]:
        raise NotImplementedError()
