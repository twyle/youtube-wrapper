from ..param_generator import ParamGenerator
from typing import Optional

class VideoCommentThreadParamGenerator(ParamGenerator):
    def __init__(self, video_id: str, max_results: Optional[int] = 10) -> None:
        self.__video_id = video_id
        self.__max_results = max_results
        
    def __call__(self) -> dict[str, str]:
        return {
            'part': 'id,snippet,replies',
            'videoId': self.__video_id,
            'maxResults': self.__max_results
        }