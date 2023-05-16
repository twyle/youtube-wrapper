from ..response_parsers import ResponseParser
from ...models.video_model import Video

class VideoResponseParser(ResponseParser):
    def __call__(self, response: dict[str, str]) -> Video:
        return self.__create_video(self.__parse_youtube_video(response))
    
    def __parse_youtube_video(self, result: dict[str, str]) -> dict[str, str]:
        parsed_video_details = dict()
        items = result['items'][0]
        parsed_video_details = dict()
        parsed_video_details['video_id'] = items['id']
        parsed_video_details['video_title'] = items['snippet']['title']
        parsed_video_details['channel_title'] = items['snippet']['channelTitle']
        parsed_video_details['video_description'] = items['snippet']['description']
        parsed_video_details['video_thumbnail'] = self.__get_thumbnail(items['snippet']['thumbnails'])
        parsed_video_details['video_duration'] = items['contentDetails']['duration']
        parsed_video_details['views_count'] = items['statistics']['viewCount']
        parsed_video_details['likes_count'] = items['statistics']['likeCount']
        parsed_video_details['comments_count'] = items['statistics']['commentCount']
        return parsed_video_details
    
    def __get_thumbnail(self, thumbnails: dict[str, str]) -> str:
        thumbnail = ''
        if thumbnails:
            if thumbnails.get('standard'):
                thumbnail = thumbnails.get('standard').get('url')
            elif thumbnails.get('medium'):
                thumbnail = thumbnails.get('medium').get('url')
            elif thumbnails.get('high'):
                thumbnail = thumbnails.get('high').get('url')
            elif thumbnails.get('default'):
                thumbnail = thumbnails.get('default').get('url')
            elif thumbnails.get('maxres'):
                thumbnail = thumbnails.get('maxres').get('url')
        return thumbnail
    
    def __create_video(self, video_data: dict[str, str]) -> Video:
        video = Video(
            video_id=video_data['video_id'],
            video_title=video_data['video_title'],
            channel_title=video_data['channel_title'],
            video_description=video_data['video_description'],
            video_thumbnail=video_data['video_thumbnail'],
            video_duration=video_data['video_duration'],
            views_count=video_data['views_count'],
            comments_count=video_data['comments_count'],
            likes_count=video_data['likes_count']
        )
        return video