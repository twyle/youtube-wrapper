from youtube import YouTube
import json
import os
from typing import Optional
from youtube.models.video_model import Video

def to_json(channels):
    with open('channels.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(channels, indent=4))
        
def save_to_channels(video: Video, file_name: Optional[str] = "kenyan_channels.json") -> None:
    kenyan_channels = []
    if video:
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                try:
                    kenyan_channels = json.loads(f.read())
                except json.decoder.JSONDecodeError:
                    pass
        with open(file_name, 'w', encoding='utf-8') as f:
            data = {
                video.channel_title: video.channel_id
            }
            if not data in kenyan_channels:
                kenyan_channels.append(data)
            f.write(json.dumps(kenyan_channels, indent=2))
            print(kenyan_channels)
    

def print_videos(videos):
    vids = []
    for video in videos:
        vid = {
            'title': video.video_title,
            'channel': video.channel_title
        }
        vids.append(vid)
    print(vids)

# client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
client_secrets_file = '/home/lyle/Downloads/temp.json'
youtube = YouTube(client_secrets_file)
youtube.authenticate()
# search_iterator = youtube.search_video('Python for beginners',max_results=2)
# videos = list(next(search_iterator))
# print(videos)
# print_videos(next(search_iterator))
# print_videos(next(search_iterator))
# print_videos(next(search_iterator))
# print(next(search_iterator))
# print_videos(list(next(search_iterator)))
# print_videos(next(search_iterator))
# print_videos(next(search_iterator))
# video = youtube.find_video_by_id('RFDK1rdJ_gg')
# print(video)
# save_to_channels(video)
# ids = ['rfscVS0vtbw', 'TFa38ONq5PY']
# youtube.find_videos(ids)
# youtube.find_most_popular_video_by_region('us')
# search_iterator = youtube.search_channel('Python for beginners',max_results=2)
# channel = youtube.find_channel_by_id('UCu8luTDe_Xxd2ahAXsCWX5g')
# print(channel.to_json())
# to_json([channel.to_dict()])
# search_iterator = youtube.search_channel('Python for beginners',max_results=2)
# print(next(search_iterator))
# channel = youtube.find_channel_by_name('GoogleDevelopers')
# channel = youtube.find_channel_by_name('@PROROBOTS')
# print(channel)
# search_iterator = youtube.find_video_comments('VSB2vjWa1LA', max_results=20)
# print(next(search_iterator))
# print(next(search_iterator))
# search_iterator = youtube.find_all_channel_comments('UCu8luTDe_Xxd2ahAXsCWX5g', max_results=20)
# print(next(search_iterator))
# print(next(search_iterator))
# search_iterator = youtube.search_playlist('Python for beginners',max_results=20)
# print(next(search_iterator))
# print(next(search_iterator))
# channel_playlists = youtube.find_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')
# print(channel_playlists)
# search_iterator = youtube.find_playlist_items('PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3', max_results=25)
# print(next(search_iterator))
# print(youtube.search())