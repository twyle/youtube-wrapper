from ..factories import FindFactory, SearchFactory
from ..param_generator import ParamGenerator
from ..resource_id_parser import ResourceIdParse
from ..response_parsers import ResponseParser
from .find_parser import FindParser
from .playlist_params_generator import (
    FindChannelPlaylistsParamGenerator,
    PlaylistSearchParamGenerator,
)
from .search_parser import SearchParser


class ChannelPlaylistsFindFactory(FindFactory):
    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id

    def get_find_params_generator(self) -> ParamGenerator:
        return FindChannelPlaylistsParamGenerator(self.__channel_id)

    def get_response_parser(self) -> ResponseParser:
        return FindParser()


class PlaylistSearchFactory(SearchFactory):
    def __init__(self, query: str, max_results=10) -> None:
        self.__query = query
        self.__max_results = max_results

    def get_search_params_generator(self) -> ParamGenerator:
        return PlaylistSearchParamGenerator(self.__query, max_result=self.__max_results)

    def get_resource_id_parser(self) -> ResourceIdParse:
        return SearchParser()

    def get_find_factory(self, video_id: str) -> FindFactory:
        return None
