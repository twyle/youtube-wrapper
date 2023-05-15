from setuptools import find_packages, setup

# For consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.0.1' 
DESCRIPTION = 'A python library that wraps around the YouTube V3 API. You can use it find and manage YouTube resources including Videos, Playlists, Channels and Comments.'

key_words = [
    'youtube', 'youtube-api', 'youtube comments', 'youtube videos',
    'youtube channels', 'youtube comment thread', 'create youtube playlist'
]

install_requires = [
    'google-api-python-client', 
    'google-auth-oauthlib'
]

setup(
    name='youtube',
    packages=find_packages(
        include=[
            'youtube',
            'youtube.oauth',
            'youtube.models',
            'youtube.resources',
            'youtube.resources.video'
        ]
        ),
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://youtube.readthedocs.io/",
    author='Lyle Okoth',
    author_email='lyceokoth@gmail.com',
    license='MIT',
    install_requires=install_requires,
    keywords=key_words,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
)