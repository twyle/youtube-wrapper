from ..param_generator import ParamGenerator

        
class FindPlaylistItemParamGenerator(ParamGenerator): 
    def __init__(self, playlist_id: str) -> None:
        self.__playlist_id = playlist_id
               
    def __call__(self) -> dict[str, str]:
        return {
            'playlistId': self.__playlist_id,
            'part': 'snippet,id,contentDetails,status',
            'maxResults': 25
        }