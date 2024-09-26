import streamlit as st
import matplotlib.pyplot as plt

st.markdown("""
# CIFAR-10 Image Classifier
""")

import torch
import os
import matplotlib.pyplot as plt
import cv2
from PIL import Image

img_file = st.file_uploader(label="upload an image", 
                            type=["png", "jpg", "jpeg"], 
                            )

if img_file is not None:
    img = Image.open(img_file)
    st.image(img, caption="Uploaded Image")

if st.button("Predict"):
    st.write("Prediction: car")
    st.write("Probability: 0.976")


   


# To run the streamlit app, open and the terminal and navigate to the 
# directory of this file, and then type:
# streamlit run st_demo.py