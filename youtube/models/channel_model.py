import datetime as dt
from dataclasses import dataclass
from typing import Optional

from .resource_saver_mixins import ResourseSaverMixin


@dataclass
class Channel(ResourseSaverMixin):
    channel_id: str
    channel_title: str
    published_at: dt.datetime
    custom_url: str
    channel_description: str
    channel_thumbnail: str
    views_count: int
    videos_count: int
    subscribers_count: Optional[int] = 0
