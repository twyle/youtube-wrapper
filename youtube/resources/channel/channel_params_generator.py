from ..param_generator import ParamGenerator


class ChannelSearchParamGenerator(ParamGenerator):
    def __init__(self, query: str, max_result: int = 10, region_code: str = 'us') -> None:
        self.__query = query
        self.__max_result = max_result
        self.__region_code = region_code
        self.__search_type = 'channel'
        
    def __call__(self) -> dict[str, str]:
        return {
            'part': 'id',
            'type': self.__search_type,
            'q': self.__query,
            'maxResults': self.__max_result,
            'regionCode': self.__region_code
        }
        
class FindChannelParamGenerator(ParamGenerator): 
    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
               
    def __call__(self) -> dict[str, str]:
        if isinstance(self.__channel_id, list):
            self.__channel_id = ','.join(self.__channel_id)
        return {
            'id': self.__channel_id,
            'part': 'snippet,contentDetails,statistics'
        }
        
class FindChannelByNameParamGenerator(ParamGenerator): 
    def __init__(self, channel_name: str) -> None:
        self.__channel_name = channel_name
               
    def __call__(self) -> dict[str, str]:
        return {
            'forUsername': self.__channel_name,
            'part': 'snippet,contentDetails,statistics'
        }