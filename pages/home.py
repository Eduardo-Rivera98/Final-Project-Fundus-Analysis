import streamlit as st
import cv2
import streamlit.components.v1 as components


def app():
   portada = cv2.imread('Datos/preprocessed_2/2_right.jpg')
   st.title('DISEASE DETECTION THROUGH EYE FUNDUS IMAGE ANALYSIS')
   st.image(portada, use_column_width=True)
   st.write("""
    ### by Eduardo Rivera
    In this project, I have built several convolutional neural networks to detect diseases through the processing of eye-fundus images
    """) 

