from typing import Any
from google.auth.exceptions import RefreshError


class Auth:        
    def __call__(self, func) -> Any:
        def wrapper(self, *args: Any, **kwds: Any):              
            # self.oauth.verify_credentials()
            x = self.oauth.save_credentials()
            print(x)
        return wrapper
    
    
