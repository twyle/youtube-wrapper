from typing import Any, Callable


class Auth:
    def __call__(self, func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        def wrapper(self, *args: Any, **kwds: Any):
            if not self.youtube_client:
                raise ValueError(
                    'The current request is not authenticated. Use "youtube.authenticate()".'
                )
            return func(self, *args, **kwds)

        return wrapper
