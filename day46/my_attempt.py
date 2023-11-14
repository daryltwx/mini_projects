import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = "YOUR CLIENT ID"
SPOTIPY_CLIENT_SECRET = "YOUR SECRET"
SPOTIPY_REDIRECT_URL = "google.com"

URL = "https://www.billboard.com/charts/hot-100/"

# step 1: Scrape top 100 song from a particular date of choice
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "1995-02-08"
billboard_response = requests.get(url=f"{URL}/{date}")
billboard_html = billboard_response.text
# print(billboard_html)

soup = BeautifulSoup(billboard_html, "html.parser")
music_title = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in music_title]
# print(song_names)

# step 2: extract all the song from the list
# step 3: spotify api to create a new playlist


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
)
)

results = sp.search(q="creep", limit=2)
# print(results)

# step 4: search through spotify and add the songs to the playlist

# Creating a playlist
spotify_user_id = "11127022264"
spotify_endpoint = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"

playlist_params = {
    "name": f"Billboard Top 100 for {date}",
    "public": False,
    "description": "Made using Billboard Top 100 list"
}


spotify_playlist = requests.post(url=spotify_endpoint, json=playlist_params)
print(spotify_playlist.text)

song_search_params = {
    "track": f"{song_names[0]}",
    "year": f"{date.split('-')[0]}"
}
song = sp.search(q=song_search_params)
song_uri = song["tracks"]["items"][0]["uri"]
print(song_uri)