import streamlit as st
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf



THRESHOLD=0.5
def camera(opencv_image):
    #input size 244x244
    resize = tf.image.resize(opencv_image, (224,224))
    #float32 is the input array datatype of model
    resize=resize.numpy().astype("float32")
    return resize
def file(opencv_image1):
    #input size 244x244
    resize= tf.image.resize(opencv_image1, (224,224))
    #float32 is the input array datatype of model
    resize=resize.numpy().astype("float32")
    return resize

  
#new_model=models.load_model("F:\Seni_aids_proj\model.tflite")

#loading model
model=tf.lite.Interpreter(model_path="model (1).tflite")
input_details = model.get_input_details()
output_details = model.get_output_details()
model.allocate_tensors()

def pred(img):
    #input imagep
    model.set_tensor(input_details[0]['index'],[img])
    #prediction
    model.invoke()
    #output of prediction
    output_arr=model.get_tensor(output_details[0]['index'])
    if np.max(output_arr):
        print( np.argmax(output_arr))
        return np.argmax(output_arr)
    else:
        return -1

def iff(pred):
    if pred==0:
        st.write("NITROGEN DEFICIENCY")
    elif pred==1:
        st.write("PHOSPHORUS DEFICIENCY")
    elif pred==2:
        st.write("POTTASIUM DEFICIENCY")
    else:
        st.write("INCONCLUSIVE RESULT!!")


select=st.selectbox("pick",["camera","upload image"])
if select=="camera":
    cam=st.camera_input("capture a photo")
    if cam is not None:
        file_bytes = np.asarray(bytearray(cam.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        camera=camera(opencv_image)
        pred=pred(camera)
        iff(pred)
        st.image(opencv_image,channels="BGR")

else:
    uploaded_file = st.file_uploader("Choose a image file", type=["jpg","png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image1= cv2.imdecode(file_bytes, 1)
        resized=file(opencv_image1)
        pred=pred(resized)
        iff(pred)
        st.image(resized.astype(int),channels="BGR")
