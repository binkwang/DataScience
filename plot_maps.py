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
    return pd.read_csv(csv_path)

def fetch_and_load_data():
    fetch_housing_data()
    data = load_housing_data()
    return data

def show_data():
    data = fetch_and_load_data()
    st.dataframe(data)

#########

def plot_map_1(img_path=TEMP_IMG_PATH):
    data = fetch_and_load_data()
    data.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4)
    # plt.show() // error: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
    img = os.path.join(img_path, "01.png")
    plt.savefig(img)
    st.image(img, width=None)

#########

def plot_map_2(img_path=TEMP_IMG_PATH):
    data = fetch_and_load_data()
    data.plot(kind="scatter", x="longitude", y="latitude",
        s=data['population']/100, label="population",
        c="median_house_value", cmap=plt.get_cmap("jet"),
        colorbar=True, alpha=0.4, figsize=(10,7),
    )
    plt.legend()
    img = os.path.join(img_path, "02.png")
    plt.savefig(img)
    st.image(img, width=None)

#########

def plot_map_3(img_path=TEMP_IMG_PATH):
    data = fetch_and_load_data()
    california_img=mpimg.imread("image/california.png") # local image
    ax = data.plot(kind="scatter", x="longitude", y="latitude", figsize=(10,7),
                        s=data['population']/100, label="Population",
                        c="median_house_value", cmap=plt.get_cmap("jet"),
                        colorbar=False, alpha=0.4,
                        )
    plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5)
    plt.ylabel("Latitude", fontsize=14)
    plt.xlabel("Longitude", fontsize=14)

    prices = data["median_house_value"]
    tick_values = np.linspace(prices.min(), prices.max(), 11)
    cbar = plt.colorbar()
    cbar.ax.set_yticklabels(["$%dk"%(round(v/1000)) for v in tick_values], fontsize=14)
    cbar.set_label('Median House Value', fontsize=16)

    plt.legend(fontsize=16)
    # plt.show()
    img = os.path.join(img_path, "03.png")
    plt.savefig(img)
    st.image(img, width=None)

#########

def plot_map_4(img_path=TEMP_IMG_PATH):
    data = fetch_and_load_data()
    california_img=mpimg.imread("image/california.png")
    ax = data.plot(kind="scatter", x="longitude", y="latitude", figsize=(10,7),
                        s=data['population']/100, label="Branch Customers",
                        c="total_bedrooms", cmap=plt.get_cmap("jet"),
                        colorbar=False, alpha=0.4,
                        )
    plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5)
    plt.ylabel("", fontsize=14)
    plt.xlabel("", fontsize=14)
    plt.tick_params(colors='w')
    plt.set_cmap("jet")

    prices = data["median_house_value"]
    cbar = plt.colorbar()
    cbar.solids.set_edgecolor("face")
    cbar.solids.set_cmap("jet")
    cbar.set_label('Churn Probability', fontsize=16, alpha=1, 
                rotation=270, labelpad=20)

    plt.legend(fontsize=16)
    # plt.show()
    img = os.path.join(img_path, "04.png")
    plt.savefig(img)
    st.image(img, width=None)

def create_temp_path():
    if not os.path.exists(TEMP_IMG_PATH):
        os.makedirs(TEMP_IMG_PATH)

#########

def run_it():
    create_temp_path()
    show_data()
    plot_map_1()
    plot_map_2()
    plot_map_3()
    plot_map_4()
