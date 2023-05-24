import os
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dataclasses import dataclass, field


@dataclass
class Oauth:
    token_file: str 
    api_service_name: str 
    api_version: str 
    scopes: list[str]  
    
    def __init__(self, clients_secret_file) -> None:
        self.token_file = "credentials.json"
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        self.__verify_client_secret_file(clients_secret_file)
        self.__clients_secret_file = clients_secret_file
        self.__credentials_path = self.__get_default_credentials_path()
        self.__credentials = None
        
    def delete_credentials_file(self) -> None:
        if os.path.exists(self.__credentials_path):
            os.remove(self.__credentials_path)
        
    def __verify_client_secret_file(self, client_secrets_file: str) -> None:
        """Verfy the client secret file."""
        if not client_secrets_file:
            raise ValueError("The clients secret file path has to be provided.")
        if not isinstance(client_secrets_file, str):
            raise TypeError("The clients secret file should be a string.")
        if not os.path.exists(client_secrets_file):
            raise ValueError(f"The path {client_secrets_file} does not exist!")
        if not self.__verify_clients_secret_file_format(client_secrets_file):
            raise ValueError('The format of the clients secret file is wrong.')
        
    def __verify_clients_secret_file_format(self, clients_secret_file) -> bool:
        """Verify the structure of the client secret file."""
        return True
    
    def __get_default_credentials_path(self):
        """Generate the default api token file location."""
        current_user_home_dir = os.path.expanduser("~")
        credentials_path = os.path.join(current_user_home_dir, self.token_file)
        return credentials_path
    
    def __credentials_to_dict(self, credentials: Credentials) -> dict:
        """Convert credentials to a dict for easy work with Flask."""
        return {
            "token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
        }
    
    def authenticate_from_clients_secret_file(self):
        """Authenticate user from the clients secret file."""
        if os.path.exists(self.__credentials_path):
            with open(self.__credentials_path, "r", encoding="utf-8") as credentials:
                self.__credentials = Credentials(**json.load(credentials))
        if not self.__credentials or not self.__credentials.valid:
            if (
                self.__credentials
                and self.__credentials.expired
                and self.__credentials.refresh_token
            ):
                self.__credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.__clients_secret_file, self.scopes
                )
                self.__credentials = flow.run_local_server(port=0)
            with open(
                self.__credentials_path, "w", encoding="utf-8"
            ) as credentials_path:
                credentials = self.__credentials_to_dict(self.__credentials)
                json.dump(credentials, credentials_path)
        youtube_api_client = build(
            self.api_service_name, self.api_version, credentials=self.__credentials
        )
        return youtube_api_client