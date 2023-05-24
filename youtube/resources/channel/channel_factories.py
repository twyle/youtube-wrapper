from ..factories import SearchFactory, FindFactory
from ..param_generator import ParamGenerator
from ..response_parsers import ResponseParser
from ..resource_id_parser import ResourceIdParse
from .channel_params_generator import ChannelSearchParamGenerator
from .search_parser import ChannelIdParser
from .channel_params_generator import FindChannelParamGenerator
from .find_parser import ChannelResponseParser

class ChannelFindFactory(FindFactory):
    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
        
    def get_find_params_generator(self) -> ParamGenerator:
        return FindChannelParamGenerator(self.__channel_id)
    
    def get_response_parser(self) -> ResponseParser:
        return ChannelResponseParser()
    
    
class ChannelSearchFactory(SearchFactory):
    def __init__(self, query: str, max_results=10) -> None:
        self.__query = query
        self.__max_results = max_results
        
    def get_search_params_generator(self) -> ParamGenerator:
        return ChannelSearchParamGenerator(self.__query, max_result=self.__max_results)

    def get_resource_id_parser(self) -> ResourceIdParse:
        return ChannelIdParser()
    
    def get_find_factory(self, channel_id: str) -> FindFactory:
        return ChannelFindFactory(channel_id)