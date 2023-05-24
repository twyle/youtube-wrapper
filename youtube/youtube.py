from .oauth import Oauth
from typing import Iterator
from .resources.video import (
    VideoResource, VideoSearchFactory, VideoFindFactory, PopularRegionVideoFactory
    )
from .models.video_model import Video
from .models.channel_model import Channel
from typing import Any, Optional
from .exceptions.exceptions import TokenExpiredException
from .resources.channel import (
    ChannelResource, ChannelSearchFactory, ChannelFindFactory, ChannelFindBynameFactory
)
from .models.comment import VideoComment, ChannelComment
from .resources.comment_thread import (
    CommentThreadResource, VideoCommentThreadSearchFactory
)
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
        self.__client_secret_file = client_secret_file
        self.__oauth = Oauth(self.__client_secret_file)
        self.__youtube_client = self.__oauth.authenticate_from_clients_secret_file()
        
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
    
    def search_video(self, query: str, max_results: Optional[int]=2) -> Iterator:
        """Search for a video using the given keywords."""
        try:
            video_search_factory = VideoSearchFactory(query, max_results=max_results)
            video_search = VideoResource(self.__youtube_client)
            search_iterator = video_search.search(video_search_factory)
        except TokenExpiredException as e:
            self.__oauth.delete_credentials_file()
            self.__youtube_client = self.__oauth.authenticate_from_clients_secret_file()
            video_search_factory = VideoSearchFactory(query, max_results=max_results)
            video_search = VideoResource(self.__youtube_client)
            search_iterator = video_search.search(video_search_factory)
        else:
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
        
    def get_ratings(self) -> None:
        """Retrieves the ratings that the authorized user gave to a list of specified videos."""
        raise NotImplementedError()
    
    def insert(self) -> None:
        """Uploads a video to YouTube and optionally sets the video's metadata."""
        raise NotImplementedError()
    
    def update(self) -> None:
        """Updates a video's metadata."""
        raise NotImplementedError()
    
    def delete(self) -> None:
        """Deletes a YouTube video."""
        raise NotImplementedError()
    
    def delete(self) -> None:
        """Deletes a YouTube video."""
        raise NotImplementedError()
    
    def rate(self) -> None:
        """Add a like or dislike rating to a video or remove a rating from a video."""
        raise NotImplementedError()
    
    def find_channel_by_id(self, channel_id: str) -> Channel:
        """Find a channel by it's id."""
        find_factory = ChannelFindFactory(channel_id)
        channel_resource = ChannelResource(self.__youtube_client)
        channel = channel_resource.find(find_factory)
        return channel
    
    def find_channel_by_name(self, channel_name: str) -> Channel:
        """Find a channel by it's name."""
        find_factory = ChannelFindBynameFactory(channel_name)
        channel_resource = ChannelResource(self.__youtube_client)
        channel = channel_resource.find(find_factory)
        return channel
    
    def find_my_channel(self) -> Channel:
        """Find the authorized user's channel."""
        raise NotImplementedError()
    
    def search_channel(self, query: str, max_results: Optional[int]=2) -> Iterator:
        """Search for a video using the given keywords."""
        channel_search_factory = ChannelSearchFactory(query, max_results=max_results)
        channel_search = ChannelResource(self.__youtube_client)
        search_iterator = channel_search.search(channel_search_factory)
        return search_iterator
    
    def find_video_comments(self, video_id: str, max_results: Optional[int] = 5) -> list[VideoComment]:
        """Get a particular video's comments."""
        video_comments_search_factory = VideoCommentThreadSearchFactory(video_id, 
                                        max_results=max_results)
        video_comments_search = CommentThreadResource(self.__youtube_client)
        search_iterator = video_comments_search.search(video_comments_search_factory)
        return search_iterator
    
    def find_channel_comments(self, channel_id: str) -> list[ChannelComment]:
        """Get a particular channels's comments."""
        pass