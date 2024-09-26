#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 23:17:49 2022

@author: aryaman

Check https://github.com/andfanilo/streamlit-drawable-canvas
for more details on how to build drawable canvas.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from joblib import dump, load
import cv2
import os
import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("Digit Recognizer")
st.markdown("""
            Try to write a digit...
            """)

model = load('convnet_for_mnist.joblib')

# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("freedraw", "transform"),
)

SIZE = 180

canvas_result = st_canvas(
    fill_color = '#000000',
    stroke_width = 20,
    stroke_color = '#FFFFFF',
    background_color = '#000000',
    height = SIZE,
    width = SIZE,
    drawing_mode = drawing_mode,
    display_toolbar = True,
    key='full_app')

input_image = canvas_result.image_data

if input_image is not None:
    # st.write(f"{type(input_image)} \t\t {input_image.shape}")
    img = cv2.resize(input_image.astype('uint8'), (28, 28))
    # st.write(f"{type(img)} \t\t {img.shape}")
    rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
    # st.write(f"{type(rescaled)} \t\t {rescaled.shape}")
    st.write('Model Input')
    st.image(rescaled)

if st.button('Predict'):
    test_x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # st.image(test_x)
    val = model.predict(test_x.reshape(1, 28, 28))
    st.write(f'Prediction: {np.argmax(val[0])}')
    # st.write(f"{val[0].shape} \t\t {type(val)} \t\t {val[0]}")
    st.bar_chart(val[0])

# st.write(canvas_result.image_data)






    
    
# To run this, open the terminal, reach the location of this program, ie,
# home/aryaman/Desktop/AI Implementation/Model Deployment/Streamlit projects/Drawing and Recognizing Digits
# and then type
# streamlit run digit_recog_interface.py



    
    
    
    
    