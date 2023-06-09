from dataclasses import dataclass, field
from ...models import Video, Playlist, Channel

resources = Video | Playlist | Channel


@dataclass
class ResourceListMixin:
    items: list[resources] = field(default_factory=list)

    def to_json(self) -> str:
        """Return json string of a list of resources."""
        pass

    def to_dict(self) -> dict[str, str | int | float]:
        """Return a dictionary of a list of resources."""
        pass
