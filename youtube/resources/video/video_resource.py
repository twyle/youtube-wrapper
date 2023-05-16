from ..resource import Resource
from ...models.video_model import Video
from typing import Any, Iterator
from ..factories import SearchFactory, FindFactory

class VideoResource(Resource[Video]):
    def __init__(self, youtube_client: Any) -> None:
        self.__youtube_client = youtube_client
        
    def search(self, search_factory: SearchFactory) -> Iterator:
        self.__search_params_generator = search_factory.get_search_params_generator()
        self.__resource_id_parser = search_factory.get_resource_id_parser()
        self.__find_factory = search_factory.get_find_factory()
        return self
    
        
    def find(self, find_factory: FindFactory, video_id: str) -> Video:
        find_video_params_generator = find_factory.get_find_params_generator()
        find_video_params = find_video_params_generator(video_id)
        result = self.__find_youtube_video(find_video_params)  
        video_parser = find_factory.get_response_parser()
        video = video_parser(result)
        return video  
            
    def __iter__(self):
        return self
    
    def __next__(self) -> list[Video]:
        return self.__search_youtube()
    
    def __search_youtube(self) -> list[Video]:
        youtube_search_request = self.__youtube_client.search().list(**self.__search_params_generator())
        youtube_search_response = youtube_search_request.execute()
        video_ids = self.__resource_id_parser(youtube_search_response)
        videos = []
        for video_id in video_ids:
            result = self.find(self.__find_factory, video_id)
            videos.append(result)
        return videos    
    
    def __find_youtube_video(self, find_params: dict[str, str]) -> dict[str, str]:
        youtube_find_request = self.__youtube_client.videos().list(
            **find_params
        )
        find_response = youtube_find_request.execute()
        return find_response
    