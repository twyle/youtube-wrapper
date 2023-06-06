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

def main():
    # channel_id = get_channel_id()
    # channel = get_channel_details(channel_id)
    # channel_playlists = get_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')
    playlists = get_playlist_items('PLouh1K1d9jkYZo8h1zPH3P1ScAWA8gxbu')
    print(playlists)

if __name__ == '__main__':
    main()