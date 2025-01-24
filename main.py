import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

## Configurando a autenticação com a API do Spotify
client_id = '2d54ad8182fd4cb486cc39027b19c773'
client_secret = 'df6591d122134f4f9505881075469dc0'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_top_tracks(region='BR', limit=20):
    
    json = sp.artist_albums('2dIgFjalVxs4ThymZ67YCE')
    
    albuns = json['items']
    
    
    album_data = []
    for item in albuns:
        album = item
        album_data.append({
           'Nome': album['name'],
           'Data de Lançamento': album['release_date'],
           'Total de Musicas': album['total_tracks']
        })
    return pd.DataFrame(album_data)


df = get_top_tracks()
        

    
    