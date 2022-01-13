# Color palette generator
import io
import requests
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from PIL import Image

def url_to_clusters(url, n_clusters = 8):

    # Download image from url
    img = Image.open(io.BytesIO(requests.get(url).content))
    img = np.array(img)

    # Reshape image into 2D array
    data = img.reshape((-1,3)).astype("float32")

    # Scale between 0 and 1
    data = data / 255

    # Perform k-means clustering
    centers = KMeans(n_clusters).fit(data).cluster_centers_

    return centers

def plot_color_palette(centers):
    plt.figure(figsize=(14,8))
    plt.imshow(centers[np.concatenate([[i] * 100 for i in range(len(centers))]).reshape((-1,10)).T])
    plt.title("Image Color Palette")
    # plt.show()

def rgb2hex(r,g,b):
    return f"{r:02x}{g:02x}{b:02x}"

def make_palette_url(palette):
    return "https://coolors.co/" + "-".join(rgb2hex(*c) for c in (palette))

