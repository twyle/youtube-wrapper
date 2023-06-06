from ..resource import Resource
from ..factories import SearchFactory, FindFactory
from typing import Iterator, Any
from ...models.playlist_item_model import PlaylistItem


class PlaylistItemResource(Resource):
    def __init__(self, youtube_client: Any) -> None:
        self.__youtube_client = youtube_client
        self.__next_page_token = None
        self.__previous_page_token = None
        
    def search(self, search_factory: SearchFactory) -> Iterator:
        self.__search_params_generator = search_factory.get_search_params_generator()
        self.__search_factory = search_factory
        return self
    
    def find(self, find_factory: FindFactory, resource_id: str) -> PlaylistItem:
        raise NotImplementedError()
    
    def __iter__(self):
        return self
    
    def __next__(self) -> list[PlaylistItem]:
        return self.__search_youtube()
    
    def __search_youtube(self) -> list[PlaylistItem]:
        search_params = self.__search_params_generator()
        if self.__next_page_token:
            search_params['pageToken'] = self.__next_page_token
        youtube_search_request = self.__youtube_client.playlistItems().list(**search_params)
        youtube_search_response = youtube_search_request.execute()
        self.__next_page_token = youtube_search_response.get('nextPageToken', '')
        find_factory = self.__search_factory.get_find_factory()
        playlist_item_parser = find_factory.get_response_parser()
        playlist_items = playlist_item_parser(youtube_search_response)
        return playlist_items