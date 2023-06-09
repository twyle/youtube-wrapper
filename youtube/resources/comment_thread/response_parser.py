from ..response_parsers import ResponseParser
from ...models.comment_model import CommentAuthor, Comment, ChannelComment, VideoComment
from ...models.comment_thread_model import VideoCommentThread, CommentThread
from typing import Any


class VideoThreadResponseParser(ResponseParser):
    def create_author(self, data: dict[str, str]) -> CommentAuthor:
        comment_author = CommentAuthor(
            author_display_name=data['author_display_name'],
            author_profile_image_url=data['author_profile_image_url'],
            author_channel_url=data['author_channel_url'],
            author_channel_id=data['author_channel_id'],
        )
        return comment_author

    def parse_comment_author(self, result: dict[str, str]) -> CommentAuthor:
        parsed_item = {}
        parsed_item['author_display_name'] = result['authorDisplayName']
        parsed_item['author_profile_image_url'] = result['authorProfileImageUrl']
        if result.get('authorChannelUrl'):
            parsed_item['author_channel_url'] = result['authorChannelUrl']
        else:
            parsed_item['author_channel_url'] = None
        if result.get('authorChannelId'):
            parsed_item['author_channel_id'] = result['authorChannelId']['value']
        else:
            parsed_item['author_channel_id'] = None
        return self.create_author(parsed_item)

    def create_comment(self, data: dict[str, Any]) -> Comment:
        comment = Comment(
            comment_id=data['comment_id'],
            comment_author=data['comment_author'],
            text_display=data['text_display'],
            text_original=data['text_original'],
            like_count=data['like_count'],
            published_at=data['published_at'],
            updated_at=data['updated_at'],
        )
        return comment

    def create_video_comment(self, data: dict[str, Any]) -> VideoComment:
        video_comment = VideoComment(
            video_id=data['video_id'], comment=self.create_comment(data)
        )
        return video_comment

    def parse_comment(self, result: dict['str', Any]) -> dict[str, Any]:
        parsed_item = {}
        parsed_item['comment_id'] = result['id']
        parsed_item['video_id'] = result['snippet']['videoId']
        parsed_item['text_display'] = result['snippet']['textDisplay']
        parsed_item['text_original'] = result['snippet']['textOriginal']
        parsed_item['comment_author'] = self.parse_comment_author(result['snippet'])
        parsed_item['like_count'] = result['snippet']['likeCount']
        parsed_item['published_at'] = result['snippet']['publishedAt']
        parsed_item['updated_at'] = result['snippet']['updatedAt']
        return self.create_video_comment(parsed_item)

    def create_comment_thread(self, data: dict[str, str]) -> CommentThread:
        comment_thread = CommentThread(
            comment_thread_id=data['comment_thread_id'],
            total_reply_count=data['total_reply_count'],
            is_public=data['is_public'],
        )
        return comment_thread

    def create_resource(self, data: dict[str, str]) -> VideoCommentThread:
        video_comment_thread = VideoCommentThread(
            video_id=data['video_id'],
            top_level_comment=data['top_level_comment'],
            comment_thread=self.create_comment_thread(data),
            replies=data['replies'],
        )
        return video_comment_thread

    def parse_resource(self, data: dict[str, Any]) -> list[VideoCommentThread]:
        comment_threads = []
        items = data['items']
        for item in items:
            parsed_item = {}
            parsed_item['comment_thread_id'] = item['id']
            parsed_item['video_id'] = item['snippet']['videoId']
            parsed_item['top_level_comment'] = self.parse_comment(
                item['snippet']['topLevelComment']
            )
            parsed_item['total_reply_count'] = item['snippet']['totalReplyCount']
            parsed_item['is_public'] = item['snippet']['isPublic']
            if item.get('replies'):
                parsed_item['replies'] = [
                    self.parse_comment(comment)
                    for comment in item['replies']['comments']
                ]
            else:
                parsed_item['replies'] = []
            comment_threads.append(parsed_item)
        return comment_threads
