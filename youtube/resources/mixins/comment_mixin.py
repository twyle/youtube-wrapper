from typing import Iterator, Optional

from ..comment_thread import (AllChannelCommentThreadSearchFactory,
                              CommentThreadResource,
                              VideoCommentThreadSearchFactory)
from .decorators import Auth


class CommentMixin:
    @Auth()
    def find_video_comments(
        self, video_id: str, max_results: Optional[int] = 5
    ) -> Iterator:
        """Get a particular video's comments."""
        video_comments_search_factory = VideoCommentThreadSearchFactory(
            video_id, max_results=max_results
        )
        video_comments_search = CommentThreadResource(self.youtube_client)
        search_iterator = video_comments_search.search(video_comments_search_factory)
        return search_iterator

    @Auth()
    def find_all_channel_comments(
        self, channel_id: str, max_results: Optional[int] = 5
    ) -> Iterator:
        """Get a particular channels's comments."""
        channel_comments_search_factory = AllChannelCommentThreadSearchFactory(
            channel_id, max_results=max_results
        )
        channel_comments_search = CommentThreadResource(self.youtube_client)
        search_iterator = channel_comments_search.search(
            channel_comments_search_factory
        )
        return search_iterator
