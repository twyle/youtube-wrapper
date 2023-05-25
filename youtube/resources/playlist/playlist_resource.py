from ..resource import Resource
from ...models.playlist_model import Playlist
from typing import Optional, Any, Iterator
from ..factories import SearchFactory, FindFactory


class PlaylistResource(Resource[Playlist]):
    def __init__(self, youtube_client: Any) -> None:
        self.__youtube_client = youtube_client
        self.__next_page_token = None
        self.__previous_page_token = None
        
    def search(self, search_factory: SearchFactory) -> Iterator:
        self.__search_params_generator = search_factory.get_search_params_generator()
        self.__resource_id_parser = search_factory.get_resource_id_parser()
        self.__search_factory = search_factory
        return self
    
    def find(self, find_factory: FindFactory) -> Playlist:
        find_playlist_params_generator = find_factory.get_find_params_generator()
        find_playlist_params = find_playlist_params_generator()
        result = self.__find_youtube_playlist(find_playlist_params)  
        playlist_parser = find_factory.get_response_parser()
        playlists = playlist_parser(result)
        return playlists 
            
    def __iter__(self):
        return self
    
    def __next__(self) -> list[Playlist]:
        return self.__search_youtube()
    
    def __search_youtube(self) -> list[Playlist]:
        search_params = self.__search_params_generator()
        if self.__next_page_token:
            search_params['pageToken'] = self.__next_page_token
        youtube_search_request = self.__youtube_client.search().list(**search_params)
        youtube_search_response = youtube_search_request.execute()
        self.__previous_page_token = youtube_search_response.get('prevPageToken', '')
        self.__next_page_token = youtube_search_response.get('nextPageToken', '')
        playlists = self.__resource_id_parser(youtube_search_response)
        return playlists   
    
    def __find_youtube_playlist(self, find_params: dict[str, str]) -> dict[str, str]:
        youtube_find_request = self.__youtube_client.playlists().list(
            **find_params
        )
        find_response = youtube_find_request.execute()
        return find_response