from abc import ABC, abstractmethod
from typing import Generic, Iterator, TypeVar, Any
from .factories import SearchFactory, FindFactory
from .mixins.resource_list import ResourceListMixin


T = TypeVar('T')

class Resource(ResourceListMixin, ABC, Generic[T]):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__()
        self.__youtube_client = youtube_client
        self.__next_page_token = None
        self.__previous_page_token = None
        
    @property
    def youtube_client(self) -> Any:
        """Get the youtube client."""
        return self.__youtube_client
    
    @property
    def next_page_token(self) -> str:
        """Get the next page token."""
        return self.__next_page_token
    
    @next_page_token.setter
    def next_page_token(self, next_page_token: str) -> None:
        """Set the next page token."""
        self.__next_page_token = next_page_token
        
    @property
    def previous_page_token(self) -> str:
        """Get the previous page token."""
        return self.__previous_page_token
    
    @previous_page_token.setter
    def previous_page_token(self, previous_page_token: str) -> None:
        """Set the previous page token."""
        self.__previous_page_token = previous_page_token
        
    def search(self, search_factory: SearchFactory) -> Iterator:
        self.__search_params_generator = search_factory.get_search_params_generator()
        self.__resource_id_parser = search_factory.get_resource_id_parser()
        self.__search_factory = search_factory
        return self
    
    def find(self, find_factory: FindFactory) -> list[T]:
        """Find videos by using their ids."""
        find_params_generator = find_factory.get_find_params_generator()
        find_params = find_params_generator()
        find_result = self.find_youtube_resource(find_params)  
        resource_parser = find_factory.get_response_parser()
        resources = resource_parser(find_result)
        return resources
    
    def __iter__(self):
        return self
    
    def __next__(self) -> list[T]:
        return self.search_youtube()
    
    def search_youtube(self) -> list[T]:
        """Search youtube for a resource given specific parameters."""
        search_params = self.__search_params_generator()
        if self.next_page_token:
            search_params['pageToken'] = self.next_page_token
        youtube_search_request = self.youtube_client.search().list(**search_params)
        youtube_search_response = youtube_search_request.execute()
        self.previous_page_token = youtube_search_response.get('prevPageToken', '')
        self.next_page_token = youtube_search_response.get('nextPageToken', '')
        resource_ids = self.__resource_id_parser(youtube_search_response)
        resources = []
        for resource_id in resource_ids:
            find_factory = self.__search_factory.get_find_factory(resource_id)
            result = self.find(find_factory)
            resources.append(result)
        self.items.extend(resources)
        return resources 
    
    @abstractmethod
    def find_youtube_resource(self, find_params: dict[str, str]) -> dict[str, str]:
        raise NotImplementedError()
