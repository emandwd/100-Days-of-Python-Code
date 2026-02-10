import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

url = f"https://www.billboard.com/charts/hot-100/{date}/"
#https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending/
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/140.0.0.0 Safari/537.36"}

response = requests.get(url=url, headers=header)
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

song_names_spans = soup.select("li ul li h3")
song_names = [
    song.get_text(strip=True)
    for song in song_names_spans
    if song.get_text(strip=True)
]
#print(song_names)

#https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth
#https://spotipy.readthedocs.io/en/2.25.1/
scope = "playlist-modify-private user-read-email"
redirect_uri= "https://example.com/callback"
SPOTIFY_CLIENT_ID = os.environ.get("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
username = os.environ.get("USERNAME")
#print(SPOTIFY_CLIENT_ID)
#print(SPOTIFY_CLIENT_SECRET)
#print(username)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    redirect_uri= redirect_uri,
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    username = username,
    cache_path="token.txt",
    show_dialog=True, #Force Spotify to show login page every time (ignore cached tokens)
    )
)
user_id = sp.current_user()["id"]
#https://spotipy.readthedocs.io/en/2.25.1/#spotipy.client.Spotify.current_user

# Use the code below anytime you need information about the currently authenticated Spotify user
user_info = sp.current_user()
name = user_info.get("display_name")  # User’s display name
email = user_info.get("email")        # User’s email (requires 'user-read-email' scope)
#print("Name:", name)
#print("Email:", email)

# Use the code below to get Spotify URIs for each song
song_uris = []
for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1) # limit=1 = “grab the first match.”
        # print(result)
        tracks = result["tracks"]["items"]
        if tracks:   # If found
            uri = tracks[0]["uri"]
            song_uris.append(uri)
            print(f"Found: {song} --> {uri}")
        else:
            print(f"Not found on Spotify: {song}")
    except Exception as e:
        print(f"Error searching for {song}: {e}")

#print("\nFinal Spotify URIs:")
#print(song_uris)

# Create a new private playlist and Add songs to the playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,                   # False = private playlist
    description=f"Billboard Hot 100 songs for {date}"
)
#print(playlist)
playlist_id = playlist["id"]
print(f"Playlist created: {playlist['name']} (ID: {playlist_id})")
if song_uris:
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
    print(f"Added {len(song_uris)} songs to your playlist!")
else:
    print("No songs found to add to the playlist.")

