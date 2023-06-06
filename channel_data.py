from youtube import YouTube

client_secret_file = '/home/downloads/client_secret.json'
youtube = YouTube(client_secret_file)
youtube.authenticate()

def get_channel_id():
    videos = youtube.find_video_by_id('pIzyo4cCGxU')
    channel_id = videos[0].channel_id
    return channel_id

def get_channel_details(channel_id):
    channel = youtube.find_channel_by_id(channel_id)
    return channel

def get_channel_playlists(channel_id):
        channel_playlists = youtube.find_channel_playlists(channel_id)
        return channel_playlists

def get_playlist_items(playlist_id):
    search_iterator = youtube.find_playlist_items(playlist_id, max_results=10)
    playlists = list(next(search_iterator))
    return playlists

def get_playlist_item_video_id(playlist_item):
    video_id = playlist_item.video_id
    return video_id

def get_videos(video_ids):
    videos = youtube.find_video_by_id(video_ids)
    return videos

def get_video_comments(video_id):
    search_iterator = youtube.find_video_comments(video_id, max_results=20)
    video_comments = list(next(search_iterator))
    return video_comments

def main():
    # channel_id = get_channel_id()
    # channel = get_channel_details(channel_id)
    # channel_playlists = get_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')
    # playlist_items = get_playlist_items('PLouh1K1d9jkYZo8h1zPH3P1ScAWA8gxbu')
    # playlist_video_ids = list(map(get_playlist_item_video_id, playlist_items))
    # playlist_videos = get_videos(playlist_video_ids)
    video_comments = get_video_comments('pIzyo4cCGxU')
    print(video_comments)

if __name__ == '__main__':
    main()