import json
from typing import Any

class ResourseSaverMixin:
    def to_dict(self) -> dict[str, Any]:
        return self.__dict__
    
    def to_json(self):
        return json.dumps(self.to_dict())