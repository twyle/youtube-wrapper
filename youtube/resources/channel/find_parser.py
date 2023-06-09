from ...models.channel_model import Channel
from ..response_parsers import ResponseParser


class ChannelResponseParser(ResponseParser):
    def parse_resource(self, result: dict[str, str]) -> dict[str, str]:
        parsed_items = []
        if result.get('items'):
            for item in result['items']:
                parsed_channel_details = dict()
                parsed_channel_details['channel_id'] = item['id']
                parsed_channel_details['channel_title'] = item['snippet']['title']
                parsed_channel_details['published_at'] = item['snippet']['publishedAt']
                parsed_channel_details['custom_url'] = item['snippet']['customUrl']
                parsed_channel_details['channel_description'] = item['snippet'][
                    'description'
                ]
                parsed_channel_details['channel_thumbnail'] = self.get_thumbnail(
                    item['snippet']['thumbnails']
                )
                if not item['statistics']['hiddenSubscriberCount']:
                    parsed_channel_details['subscribers_count'] = item['statistics'][
                        'subscriberCount'
                    ]
                parsed_channel_details['views_count'] = item['statistics']['viewCount']
                parsed_channel_details['videos_count'] = item['statistics'][
                    'videoCount'
                ]
                parsed_items.append(parsed_channel_details)
        return parsed_items

    def create_resource(self, channel_data: dict[str, str]) -> Channel:
        channel = Channel(
            channel_id=channel_data['channel_id'],
            channel_title=channel_data['channel_title'],
            published_at=channel_data['published_at'],
            channel_description=channel_data['channel_description'],
            channel_thumbnail=channel_data['channel_thumbnail'],
            videos_count=channel_data['videos_count'],
            views_count=channel_data['views_count'],
            subscribers_count=channel_data['subscribers_count'],
            custom_url=channel_data['custom_url'],
        )
        return channel
