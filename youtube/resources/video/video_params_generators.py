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