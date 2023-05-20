from .oauth import Oauth
from typing import Iterator
from .resources.video import (
    VideoResource, VideoSearchFactory, VideoFindFactory, PopularRegionVideoFactory
    )
from .models.video_model import Video
from typing import Any, Optional

class YouTube:
    """
    Provides methods for interacting with the YouTube API.
    
    This class acts as an interface to the YouTube API, providing methods for interacting with
    the YouTube V3 API. 
    
    Attributes
    ----------
    youtube_client: Any
        The object used ot interact with the YouTube V3 API.
        
    Methods
    -------
    search_video(query):
        Search for videos using the given query.
    find_video_by_id(video_id):
        Find the video with the given id.
    find_videos(video_ids):
        Find videos with the given ids.
    find_most_popular_video_by_region(region_code)
        Find the most popular videos in the given region.
    """
    def __init__(self, client_secret_file: str) -> None:
        """Create the youtube instance.
        
        Parameters
        ----------
        client_secret_file: str
            This is a string representing the path to the client secret file downloaded from 
            Google.
        """
        self.__youtube_client = self.__get_youtube_client(client_secret_file)
        
    @property
    def youtube_client(self) -> Any:
        """Get the youtube client.
        
        The youtube client is the object used to interact with the YouTube API.
        """
        return self.__youtube_client
    
    @youtube_client.setter
    def youtube_client(self, youtube_client: Any) -> None:
        """Set the youtube client."""
        raise NotImplementedError()
        
    def __get_youtube_client(self, clients_secret_file) -> None:
        """Get the youtube client."""
        oauth = Oauth(clients_secret_file)
        youtube_client = oauth.authenticate_from_clients_secret_file()
        return youtube_client
    
    def search_video(self, query: str, max_results: Optional[int]=2) -> Iterator:
        """Search for a video using the given keywords."""
        video_search_factory = VideoSearchFactory(query, max_results=max_results)
        video_search = VideoResource(self.__youtube_client)
        search_iterator = video_search.search(video_search_factory)
        return search_iterator
        
    def find_video_by_id(self, video_id: str) -> Video:
        """Find a video using its id."""
        find_factory = VideoFindFactory(video_id)
        video_resource = VideoResource(self.__youtube_client)
        video = video_resource.find(find_factory)
        return video
    
    def find_videos(self, video_ids: list[str]) -> list[Video]:
        find_factory = VideoFindFactory(video_ids)
        video_resource = VideoResource(self.__youtube_client)
        videos = video_resource.find(find_factory)
        return videos
    
    def find_most_popular_video_by_region(self, region_code: str) -> list[Video]:
        find_factory = PopularRegionVideoFactory(region_code)
        video_resource = VideoResource(self.__youtube_client)
        videos = video_resource.find(find_factory)
        return videos
    
    def find_most_popular_video_by_category(self, category_id: str) -> list[Video]:
        pass
        