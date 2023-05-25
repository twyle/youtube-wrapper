from dataclasses import dataclass, field
from typing import Optional, Any
import datetime as dt


@dataclass
class CommentAuthor:
    author_display_name: str
    author_profile_image_url: str
    author_channel_url: Optional[str] = ''
    author_channel_id: Optional[str] = ''
    
    
@dataclass
class Comment:
    comment_id: str
    comment_author: CommentAuthor
    text_display: str
    text_original: str
    like_count: int
    published_at: dt.datetime
    updated_at: dt.datetime
    parent_id: Optional[str] = ''
 
@dataclass   
class VideoComment:
    video_id: str
    comment: Comment
    
@dataclass    
class ChannelComment:
    channel_id: str
    comment: Comment