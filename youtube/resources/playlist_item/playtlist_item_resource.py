from ..resource import Resource
from ..factories import SearchFactory, FindFactory
from typing import Iterator, Any
from ...models.playlist_item_model import PlaylistItem


class PlaylistItemResource(Resource):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__(youtube_client)

    # def search(self, search_factory: SearchFactory) -> Iterator:
    #     self.__search_params_generator = search_factory.get_search_params_generator()
    #     self.__search_factory = search_factory
    #     return self

    # def find(self, find_factory: FindFactory, resource_id: str) -> PlaylistItem:
    #     raise NotImplementedError()

    # def __iter__(self):
    #     return self

    # def __next__(self) -> list[PlaylistItem]:
    #     return self.__search_youtube()

    def search_youtube(self) -> list[PlaylistItem]:
        search_params = self.search_params_generator()
        if self.next_page_token:
            search_params['pageToken'] = self.next_page_token
        youtube_search_request = self.youtube_client.playlistItems().list(
            **search_params
        )
        youtube_search_response = youtube_search_request.execute()
        self.next_page_token = youtube_search_response.get('nextPageToken', '')
        find_factory = self.search_factory.get_find_factory()
        playlist_item_parser = find_factory.get_response_parser()
        playlist_items = playlist_item_parser(youtube_search_response)
        return playlist_items

    def find_youtube_resource(self, find_params: dict[str, str]) -> dict[str, str]:
        pass
