from ..response_parsers import ResponseParser

class VideoResponseParser(ResponseParser):
    def __call__(self, response: dict[str, str]) -> dict[str, str]:
        return self.__parse_youtube_video(response)
    
    def __parse_youtube_video(self, result: dict[str, str]) -> dict[str, str]:
        parsed_video_details = dict()
        items = result['items'][0]
        parsed_video_details = dict()
        parsed_video_details['id'] = items['id']
        parsed_video_details['channelId'] = items['snippet']['channelId']
        parsed_video_details['title'] = items['snippet']['title']
        parsed_video_details['channelTitle'] = items['snippet']['channelTitle']
        parsed_video_details['description'] = items['snippet']['description']
        parsed_video_details['thumbnails'] = items['snippet']['thumbnails']
        if items['snippet'].get('tags'):
            parsed_video_details['tags'] = items['snippet']['tags']
        else:
            parsed_video_details['tags'] = []
        parsed_video_details['duration'] = items['contentDetails']['duration']
        parsed_video_details['licensedContent'] = items['contentDetails']['licensedContent']
        parsed_video_details['viewCount'] = items['statistics']['viewCount']
        parsed_video_details['likeCount'] = items['statistics']['likeCount']
        parsed_video_details['commentCount'] = items['statistics']['commentCount']
        return parsed_video_details