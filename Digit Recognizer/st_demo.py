# import streamlit as st
# import matplotlib.pyplot as plt

# st.markdown("""
# # Digit Recognizer App

# &nbsp;  
            
# Steps to use the app:

# 1. Draw a digit on a piece of paper.
# 2. Take a picture of the digit.
# 3. Upload the picture to the app, i.e., click on the 'upload' button.
# 4. Click on the 'Predict' button to predict the digit.
# """)

# uploaded_file = st.file_uploader("Choose a file")

# # change strategy: do 2 types of competitions daily
# # start with simple competitions and then move your way up

# import time

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'

import torch
import os
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("../../../Pictures/ferrari.png")
img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
print(img.shape, img.shape[-1], sep='\n')
label = "car"
prob = 0.976
plt.imshow(img)
plt.title(f"Prediction: {label}\nProbability: {prob}")
plt.axis("off")
plt.show()

