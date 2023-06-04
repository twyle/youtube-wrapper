from typing import Optional, Iterator
from .decorators import Auth

from ...models.playlist_model import Playlist
from ..playlist import (
    PlaylistSearchFactory, PlaylistResource, ChannelPlaylistsFindFactory
)
from ..playlist_item import (
    PlaylistItemResource, PlaylistItemSearchFactory
)

class PlaylistMixin:
    @Auth()
    def search_playlist(self, query: str, max_results: Optional[int]=2) -> Iterator:
        """Search for a playlist using the given keywords."""
        playlist_search_factory = PlaylistSearchFactory(query, max_results=max_results)
        playlist_search = PlaylistResource(self.youtube_client)
        search_iterator = playlist_search.search(playlist_search_factory)
        return search_iterator

    @Auth()
    def find_channel_playlists(self, channel_id: str) -> list[Playlist]:
        """Find a channel's playlists."""
        find_factory = ChannelPlaylistsFindFactory(channel_id)
        playlist_resource = PlaylistResource(self.youtube_client)
        playlists = playlist_resource.find(find_factory)
        return playlists
    
    @Auth()
    def find_playlist_items(self, playlist_id: str, max_results: Optional[int] = 5) -> Iterator:
        """Get a particular video's comments."""
        playlist_item_search_factory = PlaylistItemSearchFactory(playlist_id, 
                                        max_results=max_results)
        playlist_item_search = PlaylistItemResource(self.youtube_client)
        search_iterator = playlist_item_search.search(playlist_item_search_factory)
        return search_iterator