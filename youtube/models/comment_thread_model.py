from dataclasses import dataclass, field
from .comment_model import VideoComment, ChannelComment
from typing import Optional
from .resource_saver_mixins import ResourseSaverMixin


@dataclass
class CommentThread(ResourseSaverMixin):
    comment_thread_id: str
    total_reply_count: int
    is_public: bool


@dataclass
class VideoCommentThread(ResourseSaverMixin):
    video_id: str
    top_level_comment: VideoComment
    comment_thread: CommentThread
    replies: Optional[list[VideoComment]] = field(default_factory=list)


@dataclass
class ChannelCommentThread(ResourseSaverMixin):
    channel_id: str
    top_level_comment: ChannelComment
    comment_thread: CommentThread
    replies: Optional[list[VideoComment]] = field(default_factory=list)
