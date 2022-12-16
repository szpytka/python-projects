from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

DATE = input("Which year do you want to travel to? (YYYY-MM-DD): ")
URL = f'https://www.billboard.com/charts/hot-100/{DATE}/'
CLIENT_ID = '' # YOUR OWN CLIENT_ID FROM SPOTIFY
CLIENT_SECRET = '' # YOUR OWN CLIENT_SECRET FROM SPOTIFY

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

response = requests.get(URL).text
soup = BeautifulSoup(response, 'html.parser')

titles = []
for tag in soup.find_all('div', class_='o-chart-results-list-row-container'):
    titles.append(tag.findNext('h3').text.strip())

song_uris = []
year = DATE.split("-")[0]
for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} TOP Billboard 100 :)", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

