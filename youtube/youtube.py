from typing import Any, Optional

from .oauth import Oauth
from .resources.mixins import (ChannelMixin, CommentMixin, PlaylistMixin,
                               VideoMixin)


class YouTube(Oauth, VideoMixin, ChannelMixin, CommentMixin, PlaylistMixin):
    """
    Provides methods for interacting with the YouTube API.

    This class acts as an interface to the YouTube API, providing methods for interacting with
    the YouTube V3 API.

    Attributes
    ----------
    client_secret_file: str
        The path to the json file containing your authentication information.

    Methods
    -------
    authenticate():
        Generates the user credentials needed when querying the youtube api.
    search_video(query):
        Search for videos using the given query.
    find_video_by_id(video_id):
        Find the video with the given id.
    find_videos(video_ids):
        Find videos with the given ids.
    find_most_popular_video_by_region(region_code)
        Find the most popular videos in the given region.
    """

    def __init__(self, client_secret_file: Optional[str] = None) -> None:
        """Create the youtube instance.

        Parameters
        ----------
        client_secret_file: str
            This is a string representing the path to the client secret file downloaded from
            Google.
        """
        self.clients_secret_file = client_secret_file
        super().__init__()
