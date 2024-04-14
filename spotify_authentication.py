from datetime import datetime, timedelta
from collections import defaultdict
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read playlist-modify-public playlist-modify-private user-top-read"

def autenticar_usuario():
    auth_manager = SpotifyOAuth(scope=scope)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp