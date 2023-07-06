import streamlit as st
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf

THRESHOLD=0.5

st.title("PADDY DEFICIENCY DETECTOR")






select=st.selectbox("pick",["camera","upload image"])
if select=="camera":
    cam=st.camera_input("capture a photo")
    if cam is not None:
        file_bytes = np.asarray(bytearray(cam.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        camera=camera(opencv_image)
        pred=pred(camera)
        iff(pred)
        st.image(opencv_image,channel="RGB")

else:
    uploaded_file = st.file_uploader("Choose a image file", type=["jpg","png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image1= cv2.imdecode(file_bytes, 1)
        resized=file(opencv_image1)
        pred=pred(resized)
        iff(pred)
        st.image(resized.astype(int),channels="BGR")









