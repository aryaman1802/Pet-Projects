import streamlit as st
import matplotlib.pyplot as plt
import torch
import torch.optim as optim
import os
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from models.model1 import Model1
from utils import load_model_info, predict

st.title("Age Estimation")

device = "cuda" if torch.cuda.is_available() else "cpu"
model = Model1().to(device)
optimizer = optim.Adam(params=model.parameters(), lr=0.001)
model_name = "Model1_1.pt"
optimizer_name = "Adam_1.pt"
path = "pytorch_models"
load_model_info(path, device, model, model_name, optimizer, optimizer_name)

img_file = st.file_uploader(label="upload an image", 
                            type=["png", "jpg", "jpeg"], 
                            )

if img_file is not None:
    st.image(img_file, caption="Human image", width=256)

if st.button("Predict"):
    predicted_label, label_prob = predict(model, img_file, device)
    st.write(f"Predicted age group: {predicted_label}")
    st.write(f"Prediction Probability: {label_prob:.1f}%")


# To run the streamlit app, open and the terminal and navigate to the 
# directory of this file, and then type:
# streamlit run st_file.py
    