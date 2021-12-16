import streamlit as st
from PIL import Image
import pandas as pd
import src.calculatingmodel as funci
import cv2
import numpy as np
import src.email as em
import src.pdf as power


def app():
    st.header('Diagnosis')
    image = Image.open("Imagenes/Collage2.jpg")
    st.image(image)

    st.write("""
    ### Diagnosing disease through eye fundus image. You will recieve the probability of having the following diseases:
    * Glaucoma
    * Diabetes
    * Age-Related Macular Degeneration
    * Diabetes
    * Cataracts
    * Myopia
    
    Fill in the information below, upload the eye-fundus image in "jpeg", "jpg" or "png" format and receive your diagnosis! As well you will recieve a prediction of your age just by your eye-fundus image.
    """
    )

    Lista3=[]
    

    # Insert patient's full name
    name = st.text_input('Full Name')
    if name:
        st.write(f'Welcome to our diagnosis system {name}')
        Lista3.append('name')
        

    List=['Choose','Left eye','Right eye']
    option = st.selectbox(
    'From which eye is the image you are uploading?',
     List)
    if option!='Choose':   
        st.write(f'You selected: {option}')
        Lista3.append('option')
    
    emails=['Choose','Yes','No']
    email=st.selectbox('Do you want to recieve an email with the diagnosis?',emails)
    if email=='Yes':
        correo=st.text_input('Please introduce your email')
        Lista3.append('correo')

    uploaded_file = st.file_uploader("Choose a file to upload", type=['jpeg', 'jpg', 'png'])
    if uploaded_file:
        st.write('File successfully uploaded')
        img = Image.open(uploaded_file)
        img_path = f"Datos/FotosdeojoPac/{name} - {option}EyeFundus.jpg"
        st.image(img)
        Lista3.append('uploaded_file')
    
    
    if st.button('Submit'):
        if 'name' and 'option' and 'uploaded_file' in Lista3:
            img_path = f"Datos/FotosdeojoPac/{name} xray - {option}.jpg"
            img = img.save(img_path)
            funci.diagnose(img_path,option)
        if 'correo' in Lista3:
            
            power.create_PDF(name,correo,img_path,option)
        else:
            st.error('Missing compulsory fields')

        
            
        
    
           
        

    
    