import streamlit as st
import matplotlib.pyplot as plt
import torch
import torch.optim as optim
import os
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from models.model2 import UNet2
from utils import load_model_info, predict

st.title("Brain Tumor Segmentation")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

device = "cuda" if torch.cuda.is_available() else "cpu"
model = UNet2().to(device)
optimizer = optim.Adam(params=model.parameters(), lr=0.001)
model_name = "UNet2_1.pt"
optimizer_name = "Adam2_1.pt"
path = "pytorch_models"
load_model_info(path, device, model, model_name, optimizer, optimizer_name)

img_file = st.file_uploader(label="upload an image", 
                            type=["png", "jpg", "jpeg"], 
                            )

if img_file is not None:
    img = Image.open(img_file)
    img = img.resize((256, 256))
    ax[0].imshow(img)
    ax[0].axis("off")
    ax[0].set_title("MRI brain image")

if st.button("Predict"):
    pred_mask = predict(model, img_file, device)
    ax[1].imshow(pred_mask)
    ax[1].axis("off")
    ax[1].set_title("Binary mask predicted by a UNet model")

st.pyplot(fig)

# To run the streamlit app, open and the terminal and navigate to the 
# directory of this file, and then type:
# streamlit run st_file.py

