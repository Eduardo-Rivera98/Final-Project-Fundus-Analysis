import streamlit as st
from PIL import Image
import pandas as pd
import src.calculatingmodel as funci
import cv2
import numpy as np


def app():
    image = Image.open("Datos/preprocessed_2/1_right.jpg")
    st.image(image)

    st.write("""
    # Diagnosing disease from eye fundus image. You will recieve the probability of having the following diseases:
    (-) Glaucoma
    (-) Diabetes
    Fill in the information below, upload the eye-fundus image in "jpeg", "jpg"
    or "png" format and receive your diagnosis!
    """
    )

    # defining fields
    fields = ["name", "option","uploaded_file"]
    completed_fields = {k: None for k in fields}
    error_placeholders = dict()

    # Insert patient's full name
    name = st.text_input('Full Name')
    if name:
        st.write(f'Welcome to our diagnosis system {name}')
        completed_fields["name"] = name
    else:
        error_placeholders["name"] = st.empty()
        

    List=['Choose','Left eye','Right eye']
    option = st.selectbox(
    'From which eye is the image you are uploading?',
     List)
    if option!='Choose':   
        st.write(f'You selected: {option}')
        completed_fields['option']=option

    else:
        error_placeholders["option"] = st.empty()
        

    uploaded_file = st.file_uploader("Choose a file to upload", type=['jpeg', 'jpg', 'png'])
    if uploaded_file:
        st.write('File successfully uploaded')
        img = Image.open(uploaded_file)
        img_path = f"Datos/FotosdeojoPac/{name} - {option}EyeFundus.jpg"
        st.image(img)
        completed_fields["uploaded_file"] = uploaded_file
    else:
        error_placeholders["uploaded_file"] = st.empty()

    if st.button('Submit'):
        all_fields_completed_error = False
        for key in fields:
            if not completed_fields.get(key):
                if error_placeholders.get(key):
                    error_placeholders[key].error("Compulsory field")
                all_fields_completed_error = True
    
        if not all_fields_completed_error:
            img_path = f"Datos/FotosdeojoPac/{name} xray - {option}.jpg"
            img = img.save(img_path)
            funci.diagnose(img_path)
            
        
    
           
        

    
    