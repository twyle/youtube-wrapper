from dataclasses import dataclass
import datetime as dt
from typing import Optional


@dataclass
class Channel:
    channel_id: str
    channel_title: str
    published_at: dt.datetime
    custom_url: str
    channel_description: str
    channel_thumbnail: str
    views_count: int
    videos_count: int
    subscribers_count: Optional[int] = 0