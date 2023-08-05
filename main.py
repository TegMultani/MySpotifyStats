import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "user-library-read"

# SPOTIPY_CLIENT_ID='your-spotify-client-id'
# SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# SPOTIPY_REDIRECT_URI='your-app-redirect-url'
# SET ENVIRONMENT VARIABLES

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))





