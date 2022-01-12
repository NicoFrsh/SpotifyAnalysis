# Spotify Top Songs of 2021 Analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import spotipy as sp
import os
from spotipy.oauth2 import SpotifyClientCredentials

import explorative_analysis
import color_palette

client_id = '4036a38d6c97470f92be6d6ec4f52f6a'
os.environ['SPOTIPY_CLIENT_ID'] = client_id
client_secret = '8014d2962c5a4ca88d9334193d976f02'
os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret

spotify = sp.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Features to analyze
features_list = ['danceability','energy','valence','acousticness']

playlist_link = 'https://open.spotify.com/playlist/1umeALHvLIhU1tHaT4x9zv?si=2cafea84da9b4ad8'
# Get URI (key in link between last "/" and "?")
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
list_URIs=spotify.playlist_tracks(playlist_URI)["items"]

# Read out track uris and cover urls
track_uris = []
cover_urls = []
for x in list_URIs:
    track_uris.append(x["track"]["uri"])
    cover_urls.append(x["track"]["album"]["images"][0]["url"])

print(cover_urls[13])

centers = color_palette.url_to_clusters(cover_urls[13], n_clusters=len(features_list))

print(centers)

color_palette.plot_color_palette(centers)

# Inititalize features df by adding first song's audio features
af = spotify.audio_features(track_uris)[0]
features = pd.DataFrame.from_dict(af,orient='index').T
# Append remaining audio features to features df
for i in range(1,len(track_uris)):
    af = spotify.audio_features(track_uris)[i]
    new_feature = pd.DataFrame.from_dict(af,orient='index').T
    # print('Features of song %i extracted' %(i))
    features = features.append(new_feature)

# Set index as column and then remove it from df
features = features.reset_index(drop=True)
# Remove irrelevant columns
features = features.drop(columns=['type','id','uri','track_href','analysis_url'])
print(features.head())

explorative_analysis.plot_histograms(features, features_list, centers)
# explorative_analysis.make_barplot(features, ['danceability','energy','valence','acousticness'])

# sns.heatmap(features.astype('float').corr(), annot=True, fmt='.1g')
# plt.show()
