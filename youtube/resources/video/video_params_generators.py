from ..param_generator import ParamGenerator


class VideoSearchParamGenerator(ParamGenerator):
    def __init__(
        self, query: str, max_result: int = 10, region_code: str = 'us'
    ) -> None:
        self.__query = query
        self.__max_result = max_result
        self.__region_code = region_code
        self.__search_type = 'video'

    def __call__(self) -> dict[str, str]:
        return {
            'part': 'id',
            'type': self.__search_type,
            'q': self.__query,
            'maxResults': self.__max_result,
            'regionCode': self.__region_code,
        }


class FindVideoParamGenerator(ParamGenerator):
    def __init__(self, video_id: str) -> None:
        self.__video_id = video_id

    def __call__(self) -> dict[str, str]:
        if isinstance(self.__video_id, list):
            self.__video_id = ','.join(self.__video_id)
        return {'id': self.__video_id, 'part': 'snippet,contentDetails,statistics'}


class PopularRegionVideoParams(ParamGenerator):
    def __init__(self, region_code: str) -> None:
        self.__region_code = region_code

    def __call__(self) -> dict[str, str]:
        return {
            'chart': 'mostPopular',
            'regionCode': self.__region_code,
            'part': 'snippet,contentDetails,statistics',
        }
