from ..resource import Resource
from ...models.video_model import Video
from typing import Any, Iterator
from ..factories import SearchFactory, FindFactory
from google.auth.exceptions import RefreshError
from ...exceptions.exceptions import TokenExpiredException

class VideoResource(Resource[Video]):
    def __init__(self, youtube_client: Any) -> None:
        self.__youtube_client = youtube_client
        self.__next_page_token = None
        self.__previous_page_token = None
        
    def search(self, search_factory: SearchFactory) -> Iterator:
        self.__search_params_generator = search_factory.get_search_params_generator()
        self.__resource_id_parser = search_factory.get_resource_id_parser()
        self.__search_factory = search_factory
        return self
    
        
    def find(self, find_factory: FindFactory) -> Video:
        find_video_params_generator = find_factory.get_find_params_generator()
        find_video_params = find_video_params_generator()
        result = self.__find_youtube_video(find_video_params)  
        video_parser = find_factory.get_response_parser()
        videos = video_parser(result)
        if len(videos) == 1:
            return videos[0]
        return videos 
            
    def __iter__(self):
        return self
    
    def __next__(self) -> list[Video]:
        return self.__search_youtube()
    
    def __search_youtube(self) -> list[Video]:
        search_params = self.__search_params_generator()
        if self.__next_page_token:
            search_params['pageToken'] = self.__next_page_token
        youtube_search_request = self.__youtube_client.search().list(**search_params)
        try:
            youtube_search_response = youtube_search_request.execute()
        except RefreshError as e:
            raise TokenExpiredException('Your Token has expired. Please renew it.') from e
        self.__previous_page_token = youtube_search_response.get('prevPageToken', '')
        self.__next_page_token = youtube_search_response.get('nextPageToken', '')
        video_ids = self.__resource_id_parser(youtube_search_response)
        videos = []
        for video_id in video_ids:
            find_factory = self.__search_factory.get_find_factory(video_id)
            result = self.find(find_factory)
            videos.append(result)
        return videos   
    
    def __find_youtube_video(self, find_params: dict[str, str]) -> dict[str, str]:
        youtube_find_request = self.__youtube_client.videos().list(
            **find_params
        )
        find_response = youtube_find_request.execute()
        return find_response
    