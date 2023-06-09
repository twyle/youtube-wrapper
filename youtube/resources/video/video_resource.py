from typing import Any

from ...models.video_model import Video
from ..resource import Resource


class VideoResource(Resource[Video]):
    def __init__(self, youtube_client: Any) -> None:
        super().__init__(youtube_client)

    def find_youtube_resource(self, find_params: dict[str, str]) -> dict[str, str]:
        youtube_find_request = self.youtube_client.videos().list(**find_params)
        find_response = youtube_find_request.execute()
        return find_response
