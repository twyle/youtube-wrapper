from ..resource_id_parser import ResourceIdParse
from typing import Any
from ...models.playlist_model import Playlist

class SearchParser(ResourceIdParse):
    def __call__(self, search_response: dict[str, str]) -> list[str]:
        return self.__parse_response(search_response)
        
    def __parse_response(self, search_response: dict[str, str]) -> list[str]:
        video_ids = []
        video_results = search_response['items']
        for video_result in video_results:
            video_id = video_result['id']['videoId']
            video_ids.append(video_id)
        return video_ids
    
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

    def __create_playlist(self, data: dict[str, str]) -> list[Playlist]:
        playlist = Playlist(
            playlist_id=data['playlist_id'],
            published_at=data['published_at'],
            channel_id=data['channel_id'],
            title=data['title'],
            description=data['description'],
            thumbnail=data['thumbnail'],
            channel_title=data['channel_title']
        )
        return playlist

    def __parse_response(self, response: dict[str, Any]) -> dict[str, str]:
        playlists = []
        if response.get('items'):
            for item in response.get('items'):
                parsed_item = {}
                parsed_item['playlist_id'] = item['id']['playlistId']
                parsed_item['published_at'] = item['snippet']['publishedAt']
                parsed_item['channel_id'] = item['snippet']['channelId']
                parsed_item['title'] = item['snippet']['title']
                parsed_item['description'] = item['snippet']['description']
                parsed_item['thumbnail'] = self.__get_thumbnail(item['snippet']['thumbnails'])
                parsed_item['channel_title'] = item['snippet']['channelTitle']
                playlists.append(self.__create_playlist(parsed_item))
        return playlists