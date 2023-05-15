from youtube.resources.video import VideoResource, VideoSearchParamGenerator


search_params = VideoSearchParamGenerator('Python videos')
video_search = VideoResource('a')
x = video_search.search(search_params)
print(next(x))
print(next(x))
print(next(x))
