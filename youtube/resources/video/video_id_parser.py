from ..resource_id_parser import ResourceIdParse

class VideoIdParser(ResourceIdParse):
    def __call__(self, search_response: dict[str, str]) -> list[str]:
        return self.__parse_response(search_response)
    
    
    def __parse_response(self, search_response: dict[str, str]) -> list[str]:
        video_ids = []
        video_results = search_response['items']
        for video_result in video_results:
            video_id = video_result['id']['videoId']
            video_ids.append(video_id)
        return video_ids