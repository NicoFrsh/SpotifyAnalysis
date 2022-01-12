# Explorative Analysis
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import spotipy as sp

def plot_histograms(data, features_list, colors):

    num_plots = len(features_list)

    plt.figure()

    for i in range(num_plots):
        sub_data = data[features_list[i]]
        plt.subplot(num_plots,1,i+1)
        sns.histplot(sub_data, kde=True, stat='density', color=colors[i])
        # sns.histplot(data.danceability,kde=True,stat='density',color='darkorange')
        # plt.subplot(4,1,2)
        # sns.histplot(data.energy,kde=True,stat='density',color='darkgrey')
        # plt.subplot(4,1,3)
        # sns.histplot(data.valence,kde=True,stat='density',color='firebrick')
        # plt.subplot(4,1,4)
        # sns.histplot(data.acousticness,kde=True,stat='density',color='navy')
        # plt.tight_layout()

    plt.tight_layout()
    plt.show()

# Barplot
def make_barplot(data, features_list):
    plt.figure()
    feat_boxplot = data[['danceability','energy','valence','acousticness']]
    sns.barplot(data=feat_boxplot)
    plt.ylim(0,1)
    plt.show()

# Boxplot
def make_boxplot(data, features_list):
    plt.figure()
    feat_boxplot = data[['danceability','energy','valence','acousticness']]
    sns.boxplot(data=feat_boxplot)
    plt.show()

# Summary
def print_summary(data, features_list):
    feat_boxplot = data[['danceability','energy','valence','acousticness']]
    print(feat_boxplot.astype('float').describe())