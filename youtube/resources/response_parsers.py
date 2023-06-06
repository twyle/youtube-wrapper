from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class ResponseParser(ABC, Generic[T]):
    def __call__(self, response: dict[str, str]) -> dict[str, str]:
        parsed_items = self.parse_resource(response)
        resources = [self.create_resource(item) for item in parsed_items]
        return resources       
    
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
    
    @abstractmethod
    def parse_resource(self, result: dict[str, str]) -> dict[str, str]:
        raise NotImplementedError() 
    
    @abstractmethod
    def create_resource(self, resource_data: dict[str, str]) -> T:
        raise NotImplementedError() 
    
    