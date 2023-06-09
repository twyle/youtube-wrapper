from ..resource import Resource
from ...models.playlist_model import Playlist
from typing import Optional, Any, Iterator
from ..factories import SearchFactory, FindFactory


class PlaylistResource(Resource[Playlist]):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__(youtube_client)

    def search_youtube(self) -> list[Playlist]:
        search_params = self.__search_params_generator()
        if self.next_page_token:
            search_params['pageToken'] = self.next_page_token
        youtube_search_request = self.youtube_client.search().list(**search_params)
        youtube_search_response = youtube_search_request.execute()
        self.previous_page_token = youtube_search_response.get('prevPageToken', '')
        self.next_page_token = youtube_search_response.get('nextPageToken', '')
        playlists = self.__resource_id_parser(youtube_search_response)
        return playlists

    def find_youtube_resource(self, find_params: dict[str, str]) -> dict[str, str]:
        youtube_find_request = self.youtube_client.playlists().list(**find_params)
        find_response = youtube_find_request.execute()
        return find_response
