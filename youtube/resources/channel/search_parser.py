from ..resource_id_parser import ResourceIdParse


class ChannelIdParser(ResourceIdParse):
    def __call__(self, search_response: dict[str, str]) -> list[str]:
        return self.__parse_response(search_response)

    def __parse_response(self, search_response: dict[str, str]) -> list[str]:
        channel_ids = []
        channel_results = search_response['items']
        for channel_result in channel_results:
            channel_id = channel_result['id']['channelId']
            channel_ids.append(channel_id)
        return channel_ids
