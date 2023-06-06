.. _intro-overview:

===============
ayv at a glance
===============

ayv is a python library that enables the user to find and manage YouTube resources. 
These resources include Videos, Channels, Comments and PlayLists.

Although primarily built for searching for these resources, it can also be used to manage them,
including uploading videos, creating playlists and commenting on videos as well as answering 
other comments.


Searching for videos
====================

To show you the capabilities of this library, we will walk you through the process
of searching for videos on YouTube. The example searches for videos that deal with
python programming.

Here's the code that searches YouTube and returns an iterator:

.. code-block:: python

    from youtube import YouTube

    def search_videos():
        clients_secret_file = '/home/user/Downloads/clients_secret.json'
        youtube = YouTube(clients_secret_file)
        youtube.authenticate()
        query = 'python programming for beginners'
        video_iterator = youtube.search_video(query, max_results=2)
        print(next(video_iterator))

    if __name__ == '__main__':
        search_videos()

Put this in a text file, name it to something like ``search_videos.py``
and run it using the :command:`python` command::

    python search_videos.py


This will print a list of videos that deal with programming with Python. The
output looks like this::

    [
        Video(video_id='kqtD5dpn9C8', video_title='Python for Beginners - Learn Python in 1 Hour', 
        channel_title='Programming with Mosh', video_description='This Python tutorial for beginners show how to get started with Python quickly. Learn to code in 1 hour! Watch this tutorial get started! \n👍 Subscribe for more Python tutorials like this: https://goo.gl/6PYaGF\n🔥 Want to learn more? Watch my complete Python course: https://youtu.be/_uQrJ0TkZlc\n\n📕 Get my FREE Python cheat sheet: http://bit.ly/2Gp80s6\n\nCourses: https://codewithmosh.com\nTwitter: https://twitter.com/moshhamedani\nFacebook: https://www.facebook.com/programmingwithmosh/\nBlog: http://programmingwithmosh.com\n\n#Python, #MachineLearning, #WebDevelopment\n\n📔 Python Exercises for Beginners: https://goo.gl/1XnQB1\n\n⭐ My Favorite Python Books\n- Python Crash Course: https://amzn.to/2GqMdjG\n- Automate the Boring Stuff with Python: https://amzn.to/2N71d6S\n- A Smarter Way to Learn Python: https://amzn.to/2UZa6lE\n- Machine Learning for Absolute Beginners: https://amzn.to/2Gs0koL\n- Hands-on Machine Learning with scikit-learn and TensorFlow: https://amzn.to/2IdUuJy\n\nTABLE OF CONTENT\n\n0:00:00 Introduction \n0:00:30 What You Can Do With Python \n0:01:15 Your First Python Program \n0:05:30 Variables\n0:09:08 Receiving Input\n0:10:48 Type Conversion\n0:18:49 Strings\n0:23:41 Arithmetic Operators \n0:25:59 Operator Precedence \n0:27:11 Comparison Operators \n0:28:52 Logical Operators\n0:31:06 If Statements\n0:36:16 Exercise\n0:41:42 While Loops\n0:45:11 Lists\n0:48:47 List Methods\n0:52:16 For Loops\n0:54:54 The range() Function \n0:57:43 Tuples', 
        video_thumbnail='https://i.ytimg.com/vi/kqtD5dpn9C8/sddefault.jpg', video_duration='PT1H6S', 
        views_count='11422911', likes_count='286993', comments_count='16175'), 
        Video(video_id='rfscVS0vtbw', video_title='Learn Python - Full Course for Beginners [Tutorial]', 
        channel_title='freeCodeCamp.org', video_description="This course will give you a full introduction into all of the core concepts in python. Follow along with the videos and you'll be a python programmer in no time!\nClick the ⚙️ to change to a dub track in Spanish, Arabic, or Portuguese.\n\nWant more from Mike? He's starting a coding RPG/Bootcamp - https://simulator.dev/\n\n⭐️ Contents ⭐\n⌨️ (0:00) Introduction\n⌨️ (1:45) Installing Python & PyCharm\n⌨️ (6:40) Setup & Hello World\n⌨️ (10:23) Drawing a Shape\n⌨️ (15:06) Variables & Data Types\n⌨️ (27:03) Working With Strings\n⌨️ (38:18) Working With Numbers\n⌨️ (48:26) Getting Input From Users\n⌨️ (52:37) Building a Basic Calculator\n⌨️ (58:27) Mad Libs Game\n⌨️ (1:03:10) Lists\n⌨️ (1:10:44) List Functions\n⌨️ (1:18:57) Tuples\n⌨️ (1:24:15) Functions\n⌨️ (1:34:11) Return Statement\n⌨️ (1:40:06) If Statements\n⌨️ (1:54:07) If Statements & Comparisons\n⌨️ (2:00:37) Building a better Calculator\n⌨️ (2:07:17) Dictionaries\n⌨️ (2:14:13) While Loop\n⌨️ (2:20:21) Building a Guessing Game\n⌨️ (2:32:44) For Loops\n⌨️ (2:41:20) Exponent Function\n⌨️ (2:47:13) 2D Lists & Nested Loops\n⌨️ (2:52:41) Building a Translator\n⌨️ (3:00:18) Comments\n⌨️ (3:04:17) Try / Except\n⌨️ (3:12:41) Reading Files\n⌨️ (3:21:26) Writing to Files\n⌨️ (3:28:13) Modules & Pip\n⌨️ (3:43:56) Classes & Objects\n⌨️ (3:57:37) Building a Multiple Choice Quiz\n⌨️ (4:08:28) Object Functions\n⌨️ (4:12:37) Inheritance\n⌨️ (4:20:43) Python Interpreter\n\nCourse developed by Mike Dane. Check out his YouTube channel for more great programming courses: https://www.youtube.com/channel/UCvmINlrza7JHB1zkIOuXEbw\n\n🐦Follow Mike on Twitter - https://twitter.com/mike_dane\n\n🔗If you liked this video, Mike accepts donations on his website: https://www.mikedane.com/contribute/\n\n⭐️Other full courses by Mike Dane on our channel ⭐️\n💻C: https://youtu.be/KJgsSFOSQv0\n💻C++: https://youtu.be/vLnPwxZdW4Y\n💻SQL: https://youtu.be/HXV3zeQKqGY\n💻Ruby: https://youtu.be/t_ispmWmdjY\n💻PHP: https://youtu.be/OK_JCtrrv-c\n💻C#: https://youtu.be/GhQdlIFylQ8\n\n--\n\nLearn to code for free and get a developer job: https://www.freecodecamp.org\n\nRead hundreds of articles on programming: https://medium.freecodecamp.org", 
        video_thumbnail='https://i.ytimg.com/vi/rfscVS0vtbw/sddefault.jpg', video_duration='PT4H26M52S', 
        views_count='40202581', likes_count='970308', comments_count='43309')
    ]