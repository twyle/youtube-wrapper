from abc import ABC, abstractmethod


class ParamGenerator(ABC):
    @abstractmethod
    def __call__(self) -> dict[str, str]:
        pass
