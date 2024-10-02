from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session
import os
import spotipy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = './.flask_session/'
Session(app)

scope = "user-top-read"

SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.environ.get('SPOTIPY_REDIRECT_URI')

@app.route('/auth')
@app.route('/auth/')
def authorize():
    
    # Check if logged in, if true then change Login buttons to "Account" and "View Stats"

    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scope,
                                               cache_handler=cache_handler,
                                               show_dialog=True)
    
    if request.args.get("code"):
        # Step 2. Being redirected from Spotify auth page
        # AFTER LOGGING IN
        auth_manager.get_access_token(request.args.get("code"))
        return redirect(url_for('home_page'))

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        # Step 1. Display sign in link when no token
        auth_url = auth_manager.get_authorize_url()
        return redirect(auth_url)
    

    return redirect(url_for('home_page'))
        

    


    
@app.route('/')
@app.route('/home')
def home_page():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return render_template('home.html', logged_status=False)
    else:
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return render_template('home.html', logged_status=True, username=sp.current_user()['display_name'])

    


@app.route('/top-tracks')
def top_tracks():
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler)
    
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect(url_for('authorize'))
    else:
        sp = spotipy.Spotify(auth_manager=auth_manager)
        top_songs = []
        r = 1
        for item in sp.current_user_top_tracks(limit=50, time_range='short_term')['items']:
            l = {}
            l['rank'] = r
            print(item)
            l['image_url'] = item['album']['images'][2]['url']
            l['name'] = item['album']['name']
            artist_names = [artist["name"] for artist in item["artists"]]
            l['artists'] = ", ".join(artist_names)
            top_songs.append(l)
            r += 1

        

        return render_template('tracks.html', top_songs=top_songs)


@app.route('/sign_out')
def sign_out():
    session.pop("token_info", None)
    return redirect('/')

if __name__ == '__main__':
    app.run(threaded=True, debug=True)