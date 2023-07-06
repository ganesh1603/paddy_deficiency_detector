import streamlit as st
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf




st.title("PADDY DEFICIENCY DETECTOR")
st.subheader("TEAM MASHAN")




st.write("Hi People,This Web App Developed by TEAM MASHAN of Rajalakshmi Institute of Technology chennai.Ourself We are currently pursuing ARTIFICAL INTELLIGENCE...")
st.write("This is our first project based on CNN to detect paddy nutrient deficiency..")
st.write("This app is not 100% accurate ofcourse this app is still under development to include more feature in future")
st.write("                                          THANK YOU,")
st.write("                                                             with love")
st.write("                                                            TEAM MASHAN")



url = 'https://paddydeficiencydetectorpage1.streamlit.app/'
st.write("CLICK HERE TO CONTINUE")
st.markdown(f'''
<a href={url}><button style="background-color:black;"><text style="text-color:white;">PRESS ME</button></a>
''',
unsafe_allow_html=True)










