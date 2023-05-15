from ..resource_id_parser import ResourceIdParse

class VideoIdParser(ResourceIdParse):
    def __call__(self, search_response: dict[str, str]) -> str:
        return search_response