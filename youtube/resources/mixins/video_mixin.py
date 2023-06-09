from typing import Iterator, Optional

from ...models.video_model import Video
from ..video import PopularRegionVideoFactory, VideoFindFactory, VideoResource, VideoSearchFactory
from .decorators import Auth


class VideoMixin:
    @Auth()
    def search_video(self, query: str, max_results: Optional[int] = 2) -> Iterator:
        """Search for a video using the given keywords."""
        video_search_factory = VideoSearchFactory(query, max_results=max_results)
        video_search = VideoResource(self.youtube_client)
        search_iterator = video_search.search(video_search_factory)
        return search_iterator

    @Auth()
    def find_video_by_id(self, video_id: str) -> Video:
        """Find a video using its id."""
        find_factory = VideoFindFactory(video_id)
        video_resource = VideoResource(self.youtube_client)
        video = video_resource.find(find_factory)
        return video

    @Auth()
    def find_videos(self, video_ids: list[str]) -> list[Video]:
        find_factory = VideoFindFactory(video_ids)
        video_resource = VideoResource(self.youtube_client)
        videos = video_resource.find(find_factory)
        return videos

    @Auth()
    def find_most_popular_video_by_region(self, region_code: str) -> list[Video]:
        find_factory = PopularRegionVideoFactory(region_code)
        video_resource = VideoResource(self.youtube_client)
        videos = video_resource.find(find_factory)
        return videos

    @Auth()
    def find_most_popular_video_by_category(self, category_id: str) -> list[Video]:
        pass

    @Auth()
    def get_ratings(self) -> None:
        """Retrieves the ratings that the authorized user gave to a list of specified videos."""
        raise NotImplementedError()

    @Auth()
    def insert(self) -> None:
        """Uploads a video to YouTube and optionally sets the video's metadata."""
        raise NotImplementedError()

    @Auth()
    def update(self) -> None:
        """Updates a video's metadata."""
        raise NotImplementedError()

    @Auth()
    def delete(self) -> None:
        """Deletes a YouTube video."""
        raise NotImplementedError()

    @Auth()
    def upload(self) -> None:
        """Upload a YouTube video."""
        raise NotImplementedError()

    @Auth()
    def rate(self) -> None:
        """Add a like or dislike rating to a video or remove a rating from a video."""
        raise NotImplementedError()
