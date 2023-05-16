from youtube import YouTube

client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube = YouTube(client_secrets_file)
# youtube.search_video('Python')
# youtube.find_video_by_id('rfscVS0vtbw')
ids = ['rfscVS0vtbw', 'TFa38ONq5PY']
youtube.find_videos(ids)
