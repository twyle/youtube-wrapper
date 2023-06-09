import datetime as dt
from dataclasses import dataclass

from .resource_saver_mixins import ResourseSaverMixin


@dataclass
class PlaylistItem(ResourseSaverMixin):
    playlist_item_id: str
    date_added: dt.datetime
    channel_adder_id: str
    item_title: str
    item_description: str
    item_thumbnail: str
    channel_title: str
    video_owner_channel_title: str
    video_owner_channel_id: str
    playlist_id: str
    position: int
    video_id: str
    resource_id: str
    video_published_at: dt.datetime
    privacy_status: bool
