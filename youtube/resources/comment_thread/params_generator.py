from typing import Optional

from ..param_generator import ParamGenerator


class VideoCommentThreadParamGenerator(ParamGenerator):
    def __init__(
        self,
        video_id: str,
        max_results: Optional[int] = 10,
        order: Optional[str] = 'time',
        search_terms: Optional[str] = '',
        text_format: Optional[str] = 'html',
    ) -> None:
        self.__video_id = video_id
        self.__max_results = max_results

    def __call__(self) -> dict[str, str]:
        return {
            'part': 'id,snippet,replies',
            'videoId': self.__video_id,
            'maxResults': self.__max_results,
        }


class AllChannelCommentsThreadParamGenerator(ParamGenerator):
    def __init__(self, channel_id: str, max_results: Optional[int] = 10) -> None:
        self.__channel_id = channel_id
        self.__max_results = max_results

    def __call__(self) -> dict[str, str]:
        return {
            'part': 'snippet,replies',
            'allThreadsRelatedToChannelId': self.__channel_id,
            'maxResults': self.__max_results,
        }
