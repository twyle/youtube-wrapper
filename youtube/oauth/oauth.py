import os
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dataclasses import dataclass
from google.auth.exceptions import RefreshError
from json.decoder import JSONDecodeError
from typing import Optional


@dataclass
class Oauth:
    token_file: str 
    api_service_name: str 
    api_version: str 
    scopes: list[str]  
    
    def __init__(self) -> None:
        self.token_file = "credentials.json"
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        self.__youtube_client = None
        self.__clients_secret_file = None
        
    def delete_credentials_file(self, credentials_path: str) -> None:
        if os.path.exists(credentials_path):
            os.remove(credentials_path)
        
    def verify_client_secret_file(self, client_secrets_file: str) -> None:
        """Verfy the client secret file."""
        if not client_secrets_file:
            raise ValueError("The clients secret file path has to be provided.")
        if not isinstance(client_secrets_file, str):
            raise TypeError("The clients secret file should be a string.")
        if not os.path.exists(client_secrets_file):
            raise ValueError(f"The path {client_secrets_file} does not exist!")
        if not self.verify_clients_secret_file_format(client_secrets_file):
            raise ValueError('The format of the clients secret file is wrong.')
        
    def verify_clients_secret_file_format(self, clients_secret_file) -> bool:
        """Verify the structure of the client secret file."""
        try:
            with open(clients_secret_file, 'r', encoding='utf-8') as f:
                json.load(f)
        except JSONDecodeError:
            return False
        return True
    
    def verify_scopes(self, scopes: list[str]) -> bool:
        if not scopes:
            raise ValueError('The scopes has to be provided.')
        if not isinstance(scopes, list):
            raise TypeError('The scope has to be a list of strings.')
        return True
    
    def get_default_credentials_path(self):
        """Generate the default api token file location."""
        current_user_home_dir = os.path.expanduser("~")
        credentials_path = os.path.join(current_user_home_dir, self.token_file)
        return credentials_path
    
    def credentials_to_dict(self, credentials: Credentials) -> dict:
        """Convert credentials to a dict for easy work with Flask."""
        return {
            "token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
        }
        
    def get_credentials(self, credentials_path: str) -> Credentials:
        """Get the credentials."""
        self.verify_credentials_file(credentials_path)
        credentials = None
        with open(credentials_path, "r", encoding="utf-8") as creds:
            credentials = Credentials(**json.load(creds))
        return credentials
    
    def verify_credentials_file(self, credentials_path: str) -> bool:
        if not credentials_path:
            raise ValueError('The credentials path has to be provided.')
        if not isinstance(credentials_path, str):
            raise TypeError('The credentials path should be a string')
        if not os.path.exists(credentials_path):
            raise ValueError('The given credentials path doses ot exist.')
        try:
            with open(credentials_path, 'r', encoding='utf-8') as f:
                json.load(f)
        except JSONDecodeError:
            raise ValueError('Invalid credentials file format')
        self.verify_credentials_format(credentials_path)
        return True
        
    def verify_credentials_format(self, credentials_path: str) -> bool:
        """Ensure all the keys are present"""
        with open(credentials_path, 'r', encoding='utf-8') as f:
            credentials_dict = json.load(f)
        return True
    
    def verify_credentials(self, credentials: Credentials, api_service_name: str, api_version: str) -> bool:
        youtube_api_client = build(
            api_service_name, api_version, credentials=credentials
        )
        youtube_find_request = youtube_api_client.search().list(q='', part='id')
        try:
            youtube_find_request.execute()
        except RefreshError:
            return False
        return True
        
    def generate_credentials(self, clients_secret_file: str, scopes: list[str]) -> Credentials:
        credentials = None
        self.verify_client_secret_file(clients_secret_file)
        flow = InstalledAppFlow.from_client_secrets_file(
                clients_secret_file, scopes)
        credentials = flow.run_local_server(port=0)
        return credentials
   
    def save_credentials(self, credentials: Credentials, credentials_path: str) -> None:
        credentials_dict = self.credentials_to_dict(credentials)
        with open(credentials_path, 'w', encoding='utf-8') as f:
            json.dump(credentials_dict, f)        
            
    def get_youtube_client(self, credentials: Credentials, api_service_name: str, api_version: str):
        youtube_client = build(
            api_service_name, api_version, credentials=credentials
        )
        return youtube_client
            
    def authenticate(self, clients_secret_file: Optional[str] = ''):
        if clients_secret_file:
            self.clients_secret_file = clients_secret_file
        credentials_path = self.get_default_credentials_path()
        credentials = self.get_credentials(credentials_path)
        if not credentials or not self.verify_credentials(credentials, self.api_service_name, self.api_version):
            credentials = self.generate_credentials(self.clients_secret_file, self.scopes)
            self.verify_credentials(credentials, self.api_service_name, self.api_version)
            self.save_credentials(credentials, credentials_path)
        youtube_client = self.get_youtube_client(credentials, self.api_service_name, self.api_version)
        self.__youtube_client = youtube_client
        return self.__youtube_client