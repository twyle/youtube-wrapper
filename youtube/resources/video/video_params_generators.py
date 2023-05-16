from ..param_generator import ParamGenerator

class VideoSearchParamGenerator(ParamGenerator):
    def __init__(self, query: str, max_result: int = 10, region_code: str = 'us') -> None:
        self.__query = query
        self.__max_result = max_result
        self.__region_code = region_code
        self.__search_type = 'video'
        
    def __call__(self) -> dict[str, str]:
        return {
            'part': 'id',
            'type': self.__search_type,
            'q': self.__query,
            'maxResults': self.__max_result,
            'regionCode': self.__region_code
        }
        
class FindVideoParamGenerator(ParamGenerator):        
    def __call__(self, video_id: str | list[str]) -> dict[str, str]:
        if isinstance(video_id, list):
            video_id = ','.join(video_id)
        return {
            'id': video_id,
            'part': 'snippet,contentDetails,statistics'
        }
        