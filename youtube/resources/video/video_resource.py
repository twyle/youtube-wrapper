from ..resource import Resource
from ...models.video_model import Video
from typing import Any, Callable, Iterator

class VideoResource(Resource[Video]):
    def __init__(self, youtube_client: Any) -> None:
        self.__youtube_client = youtube_client
        self.range = 0
        
    def search(self, params_generator: Callable[..., dict]) -> Iterator:
        self.__search_params = params_generator()
        return self
        
    def find(self, resource_id: str) -> Video:
        pass
    
    def __iter__(self):
        raise NotImplementedError()
    
    def __next__(self) -> list[Video]:
        return self.__search_youtube()
    
    def __search_youtube(self) -> dict[str, str]:
        youtube_search_request = self.__youtube_client.search().list(**self.__search_params)
        youtube_search_response = youtube_search_request.execute()
        return youtube_search_response