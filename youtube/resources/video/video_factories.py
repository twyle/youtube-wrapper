from ..factories import SearchFactory, FindFactory
from ..param_generator import ParamGenerator
from .video_params_generators import (
    VideoSearchParamGenerator,
    FindVideoParamGenerator,
    PopularRegionVideoParams,
)
from .video_id_parser import VideoIdParser
from .video_parser import VideoResponseParser
from ..resource_id_parser import ResourceIdParse
from ..response_parsers import ResponseParser


class VideoFindFactory(FindFactory):
    def __init__(self, video_id: str) -> None:
        self.__video_id = video_id

    def get_find_params_generator(self) -> ParamGenerator:
        return FindVideoParamGenerator(self.__video_id)

    def get_response_parser(self) -> ResponseParser:
        return VideoResponseParser()


class PopularRegionVideoFactory(FindFactory):
    def __init__(self, region_code: str) -> None:
        self.__region_code = region_code

    def get_find_params_generator(self) -> ParamGenerator:
        return PopularRegionVideoParams(self.__region_code)

    def get_response_parser(self) -> ResponseParser:
        return VideoResponseParser()


class VideoSearchFactory(SearchFactory):
    def __init__(self, query: str, max_results=10) -> None:
        self.__query = query
        self.__max_results = max_results

    def get_search_params_generator(self) -> ParamGenerator:
        return VideoSearchParamGenerator(self.__query, max_result=self.__max_results)

    def get_resource_id_parser(self) -> ResourceIdParse:
        return VideoIdParser()

    def get_find_factory(self, video_id: str) -> FindFactory:
        return VideoFindFactory(video_id)
