from ..param_generator import ParamGenerator

class PlaylistSearchParamGenerator(ParamGenerator):
    def __init__(self, query: str, max_result: int = 10, region_code: str = 'us') -> None:
        self.__query = query
        self.__max_result = max_result
        self.__region_code = region_code
        self.__search_type = 'playlist'
        
    def __call__(self) -> dict[str, str]:
        return {
            'part': 'id,snippet',
            'type': self.__search_type,
            'q': self.__query,
            'maxResults': self.__max_result,
            'regionCode': self.__region_code
        }
        
class FindChannelPlaylistsParamGenerator(ParamGenerator): 
    def __init__(self, channel_id: str) -> None:
        self.__channel_id = channel_id
               
    def __call__(self) -> dict[str, str]:
        return {
            'channelId': self.__channel_id,
            'part': 'snippet,contentDetails,status,id',
            'maxResults': 25
        }