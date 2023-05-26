from ..response_parsers import ResponseParser
from ...models.playlist_item_model import PlaylistItem
from typing import Any

class PlaylistItemResponseParser(ResponseParser):
    def __call__(self, response: dict[str, str]) -> PlaylistItem:
        playlist_items = self.parse_response(response)
        return playlist_items
    
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

    def create_playlist_item(self, data: dict[str, Any]) -> PlaylistItem:
        playlist_item =PlaylistItem(
            playlist_item_id=data['playlist_item_id'],
            date_added=data['date_added'],
            channel_adder_id=data['channel_adder_id'],
            item_title=data['item_title'],
            item_description=data['item_description'],
            item_thumbnail=data['item_thumbnail'],
            channel_title=data['channel_title'],
            video_owner_channel_title=data['video_owner_channel_title'],
            video_owner_channel_id=data['video_owner_channel_id'],
            playlist_id=data['playlist_id'],
            position=data['position'],
            video_id=data['video_id'],
            video_published_at=data['video_published_at'],
            privacy_status=data['privacy_status'],
            resource_id=data['resource_id']
        )
        return playlist_item

    def parse_response(self, response: dict[str, Any]) -> list[PlaylistItem]:
        playlist_items = []
        if response.get('items'):
            for item in response.get('items'):
                parsed_item = {}
                parsed_item['playlist_item_id'] = item['id']
                parsed_item['date_added'] = item['snippet']['publishedAt']
                parsed_item['channel_adder_id'] = item['snippet']['channelId']
                parsed_item['item_title'] = item['snippet']['title']
                parsed_item['item_description'] = item['snippet']['description']
                parsed_item['item_thumbnail'] = self.get_thumbnail(item['snippet']['thumbnails'])
                parsed_item['channel_title'] = item['snippet']['channelTitle']
                parsed_item['playlist_id'] = item['snippet']['playlistId']
                parsed_item['position'] = item['snippet']['position']
                parsed_item['resource_id'] = item['snippet']['resourceId']['videoId']
                parsed_item['video_owner_channel_title'] = item['snippet']['videoOwnerChannelTitle']
                parsed_item['video_owner_channel_id'] = item['snippet']['videoOwnerChannelId']
                parsed_item['privacy_status'] = item['status']['privacyStatus']
                parsed_item['video_published_at'] = item['contentDetails']['videoPublishedAt']
                parsed_item['video_id'] = item['contentDetails']['videoId']
                playlist_items.append(self.create_playlist_item(parsed_item))
        return playlist_items