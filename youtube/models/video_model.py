from dataclasses import dataclass

@dataclass
class Video:
    video_id: str
    video_title: str
    channel_title: str
    video_description: str
    video_thumbnail: str
    video_duration: str
    views_count: int
    likes_count: int
    comment_count: int
    