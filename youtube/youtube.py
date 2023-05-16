from .oauth import Oauth
from typing import Iterator
from .resources.video import (
    VideoResource, VideoSearchParamGenerator, VideoIdParser, FindVideoParamGenerator,
    VideoResponseParser
    )

class YouTube:
    def __init__(self, client_secret_file: str) -> None:
        self.__youtube_client = self.__get_youtube_client(client_secret_file)
        
    def __get_youtube_client(self, clients_secret_file) -> None:
        """Get the youtube client."""
        oauth = Oauth(clients_secret_file)
        youtube_client = oauth.authenticate_from_clients_secret_file()
        return youtube_client
    
    def search_video(self, query: str) -> Iterator:
        """Search for a video using the keywords."""
        search_params = VideoSearchParamGenerator(query, max_result=5)
        find_params = FindVideoParamGenerator()
        video_id_parser = VideoIdParser()
        response_parser = VideoResponseParser()
        video_search = VideoResource(self.__youtube_client)
        search_iterator = video_search.search(search_params, video_id_parser, find_params, response_parser)
        print(next(search_iterator))
        
    def find_by_id(self):
        pass
    
    def find_most_popular(self):
        pass
    
    def find_by_category(self):
        pass
        