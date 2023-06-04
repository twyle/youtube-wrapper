from typing import Optional, Iterator
from .decorators import Auth

from ...models.channel_model import Channel
from ..channel import (
    ChannelResource, ChannelSearchFactory, ChannelFindFactory, ChannelFindBynameFactory
)

class ChannelMixin:
    @Auth()
    def find_channel_by_id(self, channel_id: str) -> Channel:
        """Find a channel by it's id."""
        find_factory = ChannelFindFactory(channel_id)
        channel_resource = ChannelResource(self.youtube_client)
        channel = channel_resource.find(find_factory)
        return channel
    
    @Auth()
    def find_channel_by_name(self, channel_name: str) -> Channel:
        """Find a channel by it's name."""
        find_factory = ChannelFindBynameFactory(channel_name)
        channel_resource = ChannelResource(self.youtube_client)
        channel = channel_resource.find(find_factory)
        return channel
    
    @Auth()
    def find_my_channel(self) -> Channel:
        """Find the authorized user's channel."""
        raise NotImplementedError()
    
    @Auth()
    def search_channel(self, query: str, max_results: Optional[int]=2) -> Iterator:
        """Search for a video using the given keywords."""
        channel_search_factory = ChannelSearchFactory(query, max_results=max_results)
        channel_search = ChannelResource(self.youtube_client)
        search_iterator = channel_search.search(channel_search_factory)
        return search_iterator