import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "Your Client ID"
SPOTIPY_CLIENT_SECRET = "Your Client Secret"
SPOTIFY_USERNAME = "YOUR SPOTIFY USERNAME"

URL = "https://www.billboard.com/charts/hot-100/"

# step 1: Scrape top 100 song from a particular date of choice
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_response = requests.get(url=f"{URL}/{date}")
billboard_html = billboard_response.text
# print(billboard_html)

soup = BeautifulSoup(billboard_html, "html.parser")
music_title = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in music_title]
# print(song_names)

# step 2: extract all the song from the list
# step 3: spotify api to create a new playlist
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME,
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

create_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard Top 100 on {date}",
    public=False,
    collaborative=False,
    description="Using python to get a list of Top 100 songs from billboard using it to create a playlist."

)
playlist_id = create_playlist['id']

add_songs = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)


