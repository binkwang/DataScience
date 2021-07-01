import os
import tarfile
from six.moves import urllib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import streamlit as st

DATASETS_URL = "https://github.com/ageron/handson-ml/raw/master/datasets"
HOUSING_URL = DATASETS_URL + "/housing/housing.tgz"

TEMP_HOUSING_DATA_PATH = "temp/datasets/housing"
TEMP_IMG_PATH = "temp/image"

#########
# https://zhuanlan.zhihu.com/p/93423829
# https://website2.readthedocs.io/beginning/04_matplotlib.html
# https://juejin.cn/post/6844904143568519176
# http://jonathansoma.com/lede/algorithms-2017/classes/fuzziness-matplotlib/how-pandas-uses-matplotlib-plus-figures-axes-and-subplots/
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
#########

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=TEMP_HOUSING_DATA_PATH):
    if not os.path.exists(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=TEMP_HOUSING_DATA_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path) # padas read data from cvs and return dataframe

def fetch_and_load_data():
    fetch_housing_data()
    dataframe = load_housing_data()
    return dataframe

def show_data(dataframe):
    st.dataframe(dataframe) # streamlit show dataframe

#########
# Pandas.DataFrame 
# plot to 
# matplotlib.pyplot ax
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
#########
def show_saved_figure(dataframe):
    fig, ax = plt.subplots()
    dataframe.plot(
        kind="scatter", 
        x="longitude", 
        y="latitude", 
        alpha=0.4, 
        ax=ax)

    # error: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
    # plt.show()

    if not os.path.exists(TEMP_IMG_PATH):
        os.makedirs(TEMP_IMG_PATH)
    img_full_path = os.path.join(TEMP_IMG_PATH, "01.png")
    plt.savefig(img_full_path)
    st.image(img_full_path, width=None) # streamlit show image

#########
# stramlit
# show 
# matplotlib.pyplot fig
#########
def plot_map_1(dataframe):
    fig, ax = plt.subplots()
    dataframe.plot(
        kind="scatter", 
        x="longitude", 
        y="latitude", 
        alpha=0.4, 
        ax=ax)
    st.pyplot(fig) # streamlit show figure

#########
# ax.set_title
# ax.legend
#########
def plot_map_2(dataframe):
    fig, ax = plt.subplots()
    dataframe.plot(
        kind="scatter", 
        x="longitude", 
        y="latitude",
        s=dataframe['population']/100, 
        label="population",
        c="median_house_value", 
        cmap=plt.get_cmap("jet"),
        colorbar=True, 
        alpha=0.4, 
        figsize=(8,6),
        ax=ax)
    ax.set_title('test title')
    ax.legend(fontsize=10)
    st.pyplot(fig)

#########
# ax.set_xlabel
# ax.set_ylabel
#########
def plot_map_3(dataframe):
    fig, ax = plt.subplots()
    california_img = mpimg.imread("image/california.png") # local image
    dataframe.plot(
        kind="scatter", 
        x="longitude", 
        y="latitude", 
        s=dataframe['population']/100, 
        label="Population",
        c="median_house_value", 
        cmap=plt.get_cmap("jet"),
        colorbar=False, 
        alpha=0.4,
        figsize=(8,6),
        ax=ax)
    ax.set_xlabel("Longitude", fontsize=10)
    ax.set_ylabel("Latitude", fontsize=10)
    ax.legend(fontsize=10)

    plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5)
    cbar = plt.colorbar()

    prices = dataframe["median_house_value"]
    tick_values = np.linspace(prices.min(), prices.max(), 10)
    cbar.ax.set_yticklabels(["$%dk"%(round(v/1000)) for v in tick_values], fontsize=10)
    
    cbar.set_label('Median House Value', fontsize=10)

    st.pyplot(fig)

#########
# 
#########
def plot_map_4(dataframe):
    fig, ax = plt.subplots()
    california_img=mpimg.imread("image/california.png")
    dataframe.plot(
        kind="scatter", 
        x="longitude", 
        y="latitude", 
        s=dataframe['population']/100, 
        label="Branch Customers",
        c="total_bedrooms", 
        cmap=plt.get_cmap("jet"),
        colorbar=False, 
        alpha=0.4, 
        figsize=(8,6),
        ax=ax)
    ax.set_xlabel("Longitude", fontsize=10)
    ax.set_ylabel("Latitude", fontsize=10)
    ax.legend(fontsize=10)

    plt.tick_params(colors='w')
    plt.set_cmap("jet")

    plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5)
    cbar = plt.colorbar()
    
    cbar.solids.set_edgecolor("face")
    cbar.solids.set_cmap("jet")
    cbar.set_label(
        "Churn Probability", 
        fontsize=10, 
        alpha=1, 
        rotation=270, 
        labelpad=20)
    
    st.pyplot(fig)

#########
# 
#########
def run_it():
    dataframe = fetch_and_load_data()
    show_data(dataframe)
    plot_map_1(dataframe)
    plot_map_2(dataframe)
    plot_map_3(dataframe)
    plot_map_4(dataframe)
