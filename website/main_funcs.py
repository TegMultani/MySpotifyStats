# TO DO
# 1. CREATE CACHE HANDLER


import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json

scope = "user-top-read"

# SPOTIPY_CLIENT_ID='your-spotify-client-id'
# SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# SPOTIPY_REDIRECT_URI='your-app-redirect-url'
# SET ENVIRONMENT VARIABLES

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')

def authorize():
    # http://127.0.0.1:5000/auth/
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def login(sp):
    sp = authorize()
    return sp.current_user()['display_name']


#  TOP ARTISTS / TOP TRACKS
# 'short_term' (4 weeks)
# 'medium_term' (6 months)
# 'long_term' (several years / all time)

# m_top50_artists_4weeks = sp.current_user_top_artists(limit=50, time_range='short_term')
# m_top50_artists_6months = sp.current_user_top_artists(limit=50, time_range='medium_term')
# m_top50_artists_alltime = sp.current_user_top_artists(limit=50, time_range='long_term')

# m_top50_tracks_4weeks = sp.current_user_top_tracks(limit=50, time_range='short_term')
# m_top50_tracks_6months = sp.current_user_top_tracks(limit=50, time_range='medium_term')
# m_top50_tracks_alltime = sp.current_user_top_tracks(limit=50, time_range='long_term')
