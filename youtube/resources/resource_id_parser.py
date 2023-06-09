from abc import ABC, abstractmethod


class ResourceIdParse(ABC):
    def __call__(self, search_response: dict[str, str]) -> list[str]:
        return self.parse_response(search_response)

    @abstractmethod
    def parse_response(self, search_response: dict[str, str]) -> list[str]:
        raise NotImplementedError()
