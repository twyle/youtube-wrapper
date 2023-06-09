from ..factories import SearchFactory, FindFactory
from ..param_generator import ParamGenerator
from ..resource_id_parser import ResourceIdParse
from ..response_parsers import ResponseParser
from .params_generator import (
    VideoCommentThreadParamGenerator,
    AllChannelCommentsThreadParamGenerator,
)
from typing import Optional
from .response_parser import VideoThreadResponseParser


class VideoCommentThreadFindFactory(FindFactory):
    def __init__(self, video_id: Optional[str] = None) -> None:
        self.__video_id = video_id

    def get_find_params_generator(self) -> ParamGenerator:
        return None

    def get_response_parser(self) -> ResponseParser:
        return VideoThreadResponseParser()


class VideoCommentThreadSearchFactory(SearchFactory):
    def __init__(self, video_id: str, max_results: Optional[int] = 10) -> None:
        self.__video_id = video_id
        self.__max_results = max_results

    def get_search_params_generator(self) -> ParamGenerator:
        return VideoCommentThreadParamGenerator(
            self.__video_id, max_results=self.__max_results
        )

    def get_resource_id_parser(self) -> ResourceIdParse:
        return None

    def get_find_factory(self, video_id: Optional[str] = None) -> FindFactory:
        return VideoCommentThreadFindFactory(video_id)


class AllChannelCommentThreadSearchFactory(SearchFactory):
    def __init__(self, channel_id: str, max_results: Optional[int] = 10) -> None:
        self.__channel_id = channel_id
        self.__max_results = max_results

    def get_search_params_generator(self) -> ParamGenerator:
        return AllChannelCommentsThreadParamGenerator(
            self.__channel_id, max_results=self.__max_results
        )

    def get_resource_id_parser(self) -> ResourceIdParse:
        return None

    def get_find_factory(self, channel_id: Optional[str] = None) -> FindFactory:
        return VideoCommentThreadFindFactory(channel_id)
