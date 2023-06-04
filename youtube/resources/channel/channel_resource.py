from ..resource import Resource
from ...models.channel_model import Channel
from ..factories import SearchFactory, FindFactory
from typing import Iterator, Any


class ChannelResource(Resource):
    def __init__(self, youtube_client: Any) -> None:
        self.__youtube_client = youtube_client
        self.__next_page_token = None
        self.__previous_page_token = None
        
    def search(self, search_factory: SearchFactory) -> Iterator:
        self.__search_params_generator = search_factory.get_search_params_generator()
        self.__resource_id_parser = search_factory.get_resource_id_parser()
        self.__search_factory = search_factory
        return self
    
    def find(self, find_factory: FindFactory) -> Channel:
        find_channel_params_generator = find_factory.get_find_params_generator()
        find_channel_params = find_channel_params_generator()
        result = self.__find_youtube_channel(find_channel_params)
        channel_parser = find_factory.get_response_parser()
        channels = channel_parser(result)
        if len(channels) == 1:
            return channels[0]
        return channels 
    
    def __iter__(self):
        return self
    
    def __next__(self) -> list[Channel]:
        return self.__search_youtube()
    
    def __search_youtube(self) -> list[Channel]:
        search_params = self.__search_params_generator()
        if self.__next_page_token:
            search_params['pageToken'] = self.__next_page_token
        youtube_search_request = self.__youtube_client.search().list(**search_params)
        youtube_search_response = youtube_search_request.execute()
        self.__previous_page_token = youtube_search_response.get('prevPageToken', '')
        self.__next_page_token = youtube_search_response.get('nextPageToken', '')
        channel_ids = self.__resource_id_parser(youtube_search_response)
        channels = []
        for channel_id in channel_ids:
            find_factory = self.__search_factory.get_find_factory(channel_id)
            result = self.find(find_factory)
            channels.append(result)
        return channels 
        
    def __find_youtube_channel(self, find_params: dict[str, str]) -> dict[str, str]:
        youtube_find_request = self.__youtube_client.channels().list(
            **find_params
        )
        find_response = youtube_find_request.execute()
        return find_response