from typing import Optional

from ..factories import FindFactory, SearchFactory
from ..param_generator import ParamGenerator
from ..resource_id_parser import ResourceIdParse
from ..response_parsers import ResponseParser
from .playlist_item_params_generator import FindPlaylistItemParamGenerator
from .response_parser import PlaylistItemResponseParser


class PlaylistItemFindFactory(FindFactory):
    def __init__(self, playlist_item_id: str) -> None:
        self.__playlist_item_id = playlist_item_id

    def get_find_params_generator(self) -> ParamGenerator:
        return None

    def get_response_parser(self) -> ResponseParser:
        return PlaylistItemResponseParser()


class PlaylistItemSearchFactory(SearchFactory):
    def __init__(self, playlist_item_id: str, max_results: Optional[int] = 10) -> None:
        self.__playlist_item_id = playlist_item_id
        self.__max_results = max_results

    def get_search_params_generator(self) -> ParamGenerator:
        return FindPlaylistItemParamGenerator(self.__playlist_item_id)

    def get_resource_id_parser(self) -> ResourceIdParse:
        return None

    def get_find_factory(self, playlist_item_id: Optional[str] = None) -> FindFactory:
        return PlaylistItemFindFactory(playlist_item_id)
