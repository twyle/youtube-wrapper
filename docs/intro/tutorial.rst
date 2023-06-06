.. _intro-tutorial:

===================
YouTube V3 Tutorial
===================

In this tutorial, we'll assume that ayv is already installed on your system. If that's not the case, 
see :ref:`intro-install`.

We are going to download data for a youtube channel by Wabosha Maxine, who is a Kenyan Youtuber. This will
include:

1. The Channel Details
2. The Channel Playlists
3. The Playlist Items
4. Videos in each playlist.
5. Comments for videos.

The tasks that we will perform include:

1. Obtaining data for various resources mentioned above.
2. Exporting the data for later use

ayv is written in Python. If you're new to the language you might want to
start by getting an idea of what the language is like, to get the most out of
ayv.

For this tutorial, you will need a valid google Account and an API key. These are 
obtained from the Google developer console.

To get the credentials follow this tutorial `<https://blog.hubspot.com/website/how-to-get-youtube-api-key>`_

Getting Channel Data 
====================

To obtain channel information, we need a channel id. To get a channel id, we will get a video from 
youtube and query it for its channel id. For this example we will use this video titled 
``'LTMYS: Trust In Your Abilities 💌 The Dapper Brother'`` published on ``June 2023`` as part of the ``LTMYS`` 
playlist on ``Wabosha Maxine's`` channel.

Get Channel id
--------------

The video id is the part after the ``v`` in a youtube video url i.e for ``https://www.youtube.com/watch?v=pIzyo4cCGxU``
the video id is ``pIzyo4cCGxU```. To get the channel id:

.. code-block:: python

    from youtube import YouTube

    client_secret_file = '/home/downloads/client_secret.json'
    youtube = YouTube(client_secret_file)
    youtube.authenticate()

    def get_channel_id():
        videos = youtube.find_video_by_id('pIzyo4cCGxU')
        channel_id = videos[0].channel_id
        print(channel_id)

    if __name__ == '__main__':
        get_channel_id()

The code snippet creates an instance of :class:`youtube.YouTube <youtube.YouTube>`
passing in a path to the downloaded ``client_secret.json`` file:

* :attr:`~youtube.Youtube.clients_secret_file`: the path to the file containing your identification
  details downloaded from Google.

* :meth:`~youtube.Youtube.authenticate`: uses the details from the client secret file to generate 
  and store your credentials. Subsequest calls to this method retrieve the stored credentials.

* :meth:`~youtube.Youtube.find_video_by_id`: returns a list of videos from youtube with the provided 
  `id`. Each video is an instance of :class:`~youtube.models.Video` with a bunch of details including the 
  `channel_id`.

* :attr:`~youtube.models.Video.channel_id`: the channel id for the channel to which this video belongs 
  to.

The ``get_channel_id`` function retrieves the first video and then prints out the channel id.

How to execute
--------------

Put this in a text file, name it to something like ``channel_data.py``
and run it using the :command:`python` command::

    python channel_data.py

When done executing, it will print the ``channel id`` to the terminal:

.. code-block:: 

    UC5WVOSvL9bc6kwCMXXeFLLw

What just happened under the hood?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First the call to ``youtube.authenticate`` generates credentials for use when querying the youtube API 
.These are then stored in your computer for use in later requests. The call also checks if the credentails 
are valid incase this is not the first time you've used the library. If the credentails are expired new 
ones are generated. This call may open a browser window that requests you to authorize the application.

The call to ``youtube.find_video_by_id`` then queries the youtube api for the given video and if it exist, 
returns the video details.

Get Channel Data
----------------

Next, let us get the channel details. Let us extend the ``channel_data.py`` script with a new 
function to get the channel details:

.. code-block:: python

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

    def main():
        channel_id = get_channel_id()
        channel = get_channel_details(channel_id)
        print(channel)

    if __name__ == '__main__':
        main()

* :meth:`~youtube.Youtube.find_channel_by_id`: takes in a channel id and returns a channel from Youtube 
  with the provided id. The `channel` is an instance of :class:`~youtube.models.Channel`

The ``get_channel_id`` method now returns the channel id.
The ``get_channel_details`` method uses the channel id to find the channel details.
The ``main`` method then uses the above two methods to find and print the channel details to the terminal.

How to execute
--------------

Run the script using the :command:`python` command::

    python channel_data.py

When done executing, it will print the channel details to the terminal:

.. code-block::

    [
        Channel(channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', channel_title='Wabosha Maxine', 
        published_at='2013-10-13T11:30:10Z', custom_url='@waboshamaxine', 
        channel_description='Hey there! Welcome to my channel. Subscribe to see all things beauty, 
        travel and lifestyle. Thanks for popping by!\n~ Wabosha \n\nProfessional inquiries: 
        beautybywabosha@gmail.com', 
        channel_thumbnail='https://yt3.ggpht.com/ytc/AGIKgqPwUCm7OLuVZeTpTxQ5QSQNA1c1K79Ne_ayzR-c3g=s240-c-k-c0x00ffffff-no-rj', 
        views_count='20800438', videos_count='377', subscribers_count='236000')
    ]

Get Channel Playlists
=====================

Now that we have a channel, as well as its details, we can get the playlists that are part of this 
channel. 

Let us extend the ``channel_data.py`` script with a new 
function to get the channel playlists:

.. code-block:: python

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

* :meth:`~youtube.Youtube.find_channel_playlists`: finds the playlists for a given channel. It returns 
  a list of instances of :class:`~youtube.models.Playlist`

The ``get_channel_playlists`` method now returns a list of playlist.

How to execute
--------------

Run the script using the :command:`python` command::

    python channel_data.py

When done executing, it will print the channel details to the terminal:

.. code-block::

    [
        Playlist(playlist_id='PLouh1K1d9jkZQE0ITJH820mS6s8J5PyxH', published_at='2022-10-12T18:15:53Z', 
        channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', playlist_title='VLOGS', playlist_description='', 
        playlist_thumbnail='https://i.ytimg.com/vi/EcRg4X1ftrQ/sddefault.jpg', 
        channel_title='Wabosha Maxine', privacy_status='public', videos_count=355), 
        Playlist(playlist_id='PLouh1K1d9jkbKgYLnO8csSJONqCBxM7Bj', published_at='2022-02-02T20:39:46Z', 
        channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', playlist_title='TUMA PIN', playlist_description='', 
        playlist_thumbnail='https://i.ytimg.com/vi/qVHhcn_r3bs/sddefault.jpg', 
        channel_title='Wabosha Maxine', privacy_status='public', videos_count=5), 
        Playlist(playlist_id='PLouh1K1d9jkYZo8h1zPH3P1ScAWA8gxbu', published_at='2021-08-19T08:49:34Z', 
        channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', playlist_title='LTMYS', playlist_description='', 
        playlist_thumbnail='https://i.ytimg.com/vi/27FnpZNmJ8M/mqdefault.jpg', 
        channel_title='Wabosha Maxine', privacy_status='public', videos_count=21), 
        Playlist(playlist_id='PLouh1K1d9jkbgO4hIHvabpyxUTqruqFq-', published_at='2018-08-11T13:28:00Z', 
        channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', playlist_title='MAKE-UP REVIEWS', playlist_description='', 
        playlist_thumbnail='https://i.ytimg.com/img/no_thumbnail.jpg', channel_title='Wabosha Maxine', 
        privacy_status='public', videos_count=0), 
        Playlist(playlist_id='PLouh1K1d9jkaepF8uq2aEZt-fF4KasycG', published_at='2018-08-11T13:26:21Z', 
        channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', playlist_title='FOOD REVIEWS', playlist_description='', 
        playlist_thumbnail='https://i.ytimg.com/img/no_thumbnail.jpg', channel_title='Wabosha Maxine', 
        privacy_status='public', videos_count=0), 
        Playlist(playlist_id='PLouh1K1d9jkbac3J9sOkkvTGiA-6xZ5BD', published_at='2018-05-25T16:37:00Z', 
        channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', playlist_title='HAULS', playlist_description='', 
        playlist_thumbnail='https://i.ytimg.com/img/no_thumbnail.jpg', channel_title='Wabosha Maxine', 
        privacy_status='public', videos_count=0)        
    ]

Get Playlist Items
==================

Each playlist in a YouTube channel has various items, known as playlist Items. The playlist Item contains 
information such as when the item was added to the playlist, by who , the video as well as the channel to 
which the video belongs to. 

Let us extend the ``channel_data.py`` script with a new 
function to get a single playlist's items:

.. code-block:: python

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

* :meth:`~youtube.Youtube.find_playlist_items`: finds the playlist items for a given playlist. It returns 
  an iterator. 

The ``get_playlist_items`` method returns a list of :class:`~youtube.models.PlaylistItem` by iterating through 
the results returned by the call to :meth:`~youtube.Youtube.find_playlist_items`

.. code-block:: 
    
    [
        PlaylistItem(
        playlist_item_id='UExvdWgxSzFkOWprWVpvOGgxelBIM1AxU2NBV0E4Z3hidS41NkI0NEY2RDEwNTU3Q0M2', 
        date_added='2021-08-19T08:49:42Z', 
        channel_adder_id='UC5WVOSvL9bc6kwCMXXeFLLw', 
        item_title='SOMETHING IS COOKING // Wabosha Maxine', 
        item_description='MENTIONED IN THIS VIDEO:\n-Get yourself some of the merch in this', 
        item_thumbnail='https://i.ytimg.com/vi/27FnpZNmJ8M/mqdefault.jpg', 
        channel_title='Wabosha Maxine', video_owner_channel_title='Wabosha Maxine', 
        video_owner_channel_id='UC5WVOSvL9bc6kwCMXXeFLLw', 
        playlist_id='PLouh1K1d9jkYZo8h1zPH3P1ScAWA8gxbu', position=0, video_id='27FnpZNmJ8M', 
        resource_id='27FnpZNmJ8M', video_published_at='2021-08-19T08:51:27Z', 
        privacy_status='public')
    ]