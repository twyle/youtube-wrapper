from youtube import YouTube

def print_videos(videos):
    vids = []
    for video in videos:
        vid = {
            'title': video.video_title,
            'channel': video.channel_title
        }
        vids.append(vid)
    print(vids)

client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube = YouTube(client_secrets_file)
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
# youtube.find_video_by_id('rfscVS0vtbw')
# ids = ['rfscVS0vtbw', 'TFa38ONq5PY']
# youtube.find_videos(ids)
# youtube.find_most_popular_video_by_region('us')
# search_iterator = youtube.search_channel('Python for beginners',max_results=2)
# channel = youtube.find_channel_by_id('UCCezIgC97PvUuR4_gbFUs5g')
search_iterator = youtube.search_channel('Python for beginners',max_results=2)
print(next(search_iterator))
