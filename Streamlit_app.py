import streamlit as st
import os
import requests
from zipfile import ZipFile
import glob
from dataclasses import dataclass, field
import random
import numpy as np
import cv2
import tensorflow as tf
import keras_cv
import matplotlib.pyplot as plt

def system_config(SEED_VALUE):
    # Set python `random` seed.
    # Set `numpy` seed
    # Set `tensorflow` seed.
    random.seed(SEED_VALUE)
    tf.keras.utils.set_random_seed(SEED_VALUE)
    os.environ["CUDA_VISIBLE_DEVICES"] = '0'
    os.environ['TF_CUDNN_DETERMINISTIC'] = '1'     
    os.environ['TF_USE_CUDNN'] = "true"

# Download and dataset.
def download_and_unzip(url, save_path):

    print("Downloading and extracting assets...", end="")
    file = requests.get(url)
    open(save_path, "wb").write(file.content)

    try:
        # Extract tarfile.
        if save_path.endswith(".zip"):
            with ZipFile(save_path) as zip:
                zip.extractall(os.path.split(save_path)[0])

        print("Done")
    except:
        print("Invalid file")

def app():
    system_config(SEED_VALUE=42)

    st.write('Streamlit ready.')
    if st.button("Begin"):
        DATASET_URL = r"https://www.dropbox.com/scl/fi/9k8t9619b4x0hegued5c5/Water-Bodies-Dataset.zip?rlkey=tjgepcai6t74yynmx7tqsm7af&dl=1"
        DATASET_DIR = "Water-Bodies-Dataset"
        DATASET_ZIP_PATH = os.path.join(os.getcwd(), f"{DATASET_DIR}.zip")

        # Download if dataset does not exists.
        if not os.path.exists(DATASET_DIR):
            download_and_unzip(DATASET_URL, DATASET_ZIP_PATH)
            os.remove(DATASET_ZIP_PATH)


#run the app
if __name__ == "__main__":
    app()