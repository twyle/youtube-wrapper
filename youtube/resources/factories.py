from abc import ABC, abstractmethod
from .param_generator import ParamGenerator
from .resource_id_parser import ResourceIdParse
from .response_parsers import ResponseParser


class FindFactory(ABC):
    @abstractmethod
    def get_find_params_generator(self) -> ParamGenerator:
        pass

    @abstractmethod
    def get_response_parser(self) -> ResponseParser:
        pass


class SearchFactory(ABC):
    @abstractmethod
    def get_search_params_generator(self) -> ParamGenerator:
        pass

    @abstractmethod
    def get_resource_id_parser(self) -> ResourceIdParse:
        pass

    @abstractmethod
    def get_find_factory(self, resource_id: str) -> FindFactory:
        pass
