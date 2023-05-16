from ..resource import Resource
from ...models.video_model import Video
from typing import Any, Callable, Iterator

class VideoResource(Resource[Video]):
    def __init__(self, youtube_client: Any) -> None:
        self.__youtube_client = youtube_client
        
    def search(self, params_generator: Callable[..., dict],
               resource_id_parser: Callable[[dict[str, str]], str],
               find_params_generator: Callable[..., dict],
               response_parser: Callable[..., dict]) -> Iterator:
        self.__search_params = params_generator()
        self.__resource_id_parser = resource_id_parser
        self.__find_params_generator = find_params_generator
        self.__response_parser = response_parser
        return self
        
    def find(self, params_generator: Callable[..., dict], video_id: str, 
             response_parser: Callable[[dict], dict]) -> Video:
        find_video_params = params_generator(video_id)
        result = self.__find_youtube_video(find_video_params)    
        x = response_parser(result)
        return x    
            
    def __iter__(self):
        return self
    
    def __next__(self) -> list[Video]:
        return self.__search_youtube()
    
    def __search_youtube(self) -> dict[str, str]:
        youtube_search_request = self.__youtube_client.search().list(**self.__search_params)
        youtube_search_response = youtube_search_request.execute()
        video_ids = self.__resource_id_parser(youtube_search_response)
        videos = []
        for video_id in video_ids:
            result = self.find(self.__find_params_generator, video_id, self.__response_parser)
            videos.append(result)
        return videos
    
    
    def __find_youtube_video(self, find_params: dict[str, str]) -> dict[str, str]:
        youtube_find_request = self.__youtube_client.videos().list(
            **find_params
        )
        find_response = youtube_find_request.execute()
        return find_response
    