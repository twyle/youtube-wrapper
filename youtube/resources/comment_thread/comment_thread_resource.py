from ..resource import Resource
from ..factories import SearchFactory, FindFactory
from typing import Iterator, Any
from ...models.comment_thread_model import CommentThread
from ...models.comment_thread_model import VideoCommentThread


class CommentThreadResource(Resource):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__(youtube_client)
        
    # def search(self, search_factory: SearchFactory) -> Iterator:
    #     self.__search_params_generator = search_factory.get_search_params_generator()
    #     self.__search_factory = search_factory
    #     return self
    
    # def find(self, find_factory: FindFactory, resource_id: str) -> VideoCommentThread:
    #     raise NotImplementedError()
    
    # def __iter__(self):
    #     raise NotImplementedError()
    
    # def __next__(self) -> list[CommentThread]:
    #     return self.__search_youtube()
    
    def search_youtube(self) -> list[VideoCommentThread]:
        search_params = self.search_params_generator()
        if self.next_page_token:
            search_params['pageToken'] = self.next_page_token
        youtube_search_request = self.youtube_client.commentThreads().list(**search_params)
        youtube_search_response = youtube_search_request.execute()
        self.next_page_token = youtube_search_response.get('nextPageToken', '')
        find_factory = self.search_factory.get_find_factory()
        video_comment_thread_parser = find_factory.get_response_parser()
        video_comment_threads = video_comment_thread_parser(youtube_search_response)
        return video_comment_threads
    
    def find_youtube_resource(self, find_params: dict[str, str]) -> dict[str, str]:
        pass