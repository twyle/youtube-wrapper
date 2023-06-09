from ..resource_id_parser import ResourceIdParse
from typing import Any
from ...models.playlist_model import Playlist


class FindParser(ResourceIdParse):
    def create_playlist(self, data: dict[str, str]) -> list[Playlist]:
        playlist = Playlist(
            playlist_id=data['playlist_id'],
            published_at=data['published_at'],
            channel_id=data['channel_id'],
            playlist_title=data['playlist_title'],
            playlist_description=data['playlist_description'],
            playlist_thumbnail=data['playlist_thumbnail'],
            channel_title=data['channel_title'],
            privacy_status=data['privacy_status'],
            videos_count=data['videos_count'],
        )
        return playlist

    def parse_response(self, response: dict[str, Any]) -> dict[str, str]:
        playlists = []
        if response.get('items'):
            for item in response.get('items'):
                parsed_item = {}
                parsed_item['playlist_id'] = item['id']
                parsed_item['published_at'] = item['snippet']['publishedAt']
                parsed_item['channel_id'] = item['snippet']['channelId']
                parsed_item['playlist_title'] = item['snippet']['title']
                parsed_item['playlist_description'] = item['snippet']['description']
                parsed_item['playlist_thumbnail'] = self.get_thumbnail(
                    item['snippet']['thumbnails']
                )
                parsed_item['channel_title'] = item['snippet']['channelTitle']
                parsed_item['privacy_status'] = item['status']['privacyStatus']
                parsed_item['videos_count'] = item['contentDetails']['itemCount']
                playlists.append(self.create_playlist(parsed_item))
        return playlists

    def get_thumbnail(self, thumbnails: dict[str, str]) -> str:
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
