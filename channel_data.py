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

def main():
    # channel_id = get_channel_id()
    # channel = get_channel_details(channel_id)
    channel_playlists = get_channel_playlists('UC5WVOSvL9bc6kwCMXXeFLLw')
    print(channel_playlists)

if __name__ == '__main__':
    main()