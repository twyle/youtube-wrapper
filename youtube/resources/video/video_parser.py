from ...models.video_model import Video
from ..response_parsers import ResponseParser


class VideoResponseParser(ResponseParser[Video]):
    def parse_resource(self, result: dict[str, str]) -> dict[str, str]:
        parsed_items = []
        for item in result['items']:
            parsed_video_details = dict()
            parsed_video_details['video_id'] = item['id']
            parsed_video_details['video_title'] = item['snippet']['title']
            parsed_video_details['published_at'] = item['snippet']['publishedAt']
            parsed_video_details['channel_id'] = item['snippet']['channelId']
            parsed_video_details['channel_title'] = item['snippet']['channelTitle']
            parsed_video_details['video_description'] = item['snippet']['description']
            parsed_video_details['video_thumbnail'] = self.get_thumbnail(
                item['snippet']['thumbnails']
            )
            parsed_video_details['video_duration'] = item['contentDetails']['duration']
            parsed_video_details['views_count'] = item['statistics']['viewCount']
            parsed_video_details['likes_count'] = item['statistics']['likeCount']
            parsed_video_details['comments_count'] = item['statistics']['commentCount']
            parsed_items.append(parsed_video_details)
        return parsed_items

    def create_resource(self, video_data: dict[str, str]) -> Video:
        video = Video(
            video_id=video_data['video_id'],
            video_title=video_data['video_title'],
            channel_id=video_data['channel_id'],
            channel_title=video_data['channel_title'],
            video_description=video_data['video_description'],
            video_thumbnail=video_data['video_thumbnail'],
            video_duration=video_data['video_duration'],
            views_count=video_data['views_count'],
            comments_count=video_data['comments_count'],
            likes_count=video_data['likes_count'],
            published_at=video_data['published_at'],
        )
        return video
