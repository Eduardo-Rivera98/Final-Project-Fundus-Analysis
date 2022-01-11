import streamlit as st
import src.calculatingmodel as funcion
from PIL import Image

def app():
    st.header('Checking the model')
    image = Image.open("Imagenes/Collage3.jpg")
    st.image(image)
    st.subheader('Here you will be able to choose any image from our compiled data which is labeled with a number between 1-6300, and compare the predicted results with our models against the real results.')
    number=st.text_input('Please introduce a number between 1-6300')
    if number:
        funcion.diagnose2(number)
