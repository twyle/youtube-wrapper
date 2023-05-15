from youtube import YouTube

client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube = YouTube(client_secrets_file)
youtube.search_video('Python')