from dataclasses import dataclass
import datetime as dt
from typing import Optional


@dataclass
class Playlist:
    playlist_id: str
    published_at: dt.datetime
    channel_id: str
    title: str
    description: str
    thumbnail: str
    channel_title: str
    privacy_status: Optional[bool] = False
    item_count: Optional[int] = 0