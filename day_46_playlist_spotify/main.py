import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
USERNAME = os.getenv("USERNAME")

input_date = input("Which year do you want to travel to? Type the year in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{input_date}"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

response = requests.get(url=url, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.select("li ul li h3")
songs_titles = [song.getText().strip() for song in all_songs]
print(songs_titles)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        show_dialog=True,
        cache_path=".cache",
    ))

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = input_date.split("-")[0]  # Extract the year from the input

for song in songs_titles:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
        track_items = result["tracks"]["items"]
        if track_items:
            uri = track_items[0]["uri"]
            song_uris.append(uri)
        else:
            print(f"🔍 Song not found on Spotify: {song}")
    except Exception as e:
        print(f"⚠️ Error searching for '{song}': {e}")

print("\n✅ Found URIs:")
pprint(song_uris)
