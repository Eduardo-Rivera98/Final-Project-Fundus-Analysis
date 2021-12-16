import streamlit as st
import cv2
import streamlit.components.v1 as component
from PIL import Image


def app():
   
   header = st.container()
   image=st.container()
   text=st.expander("""More Information About Eye fundus images and the models used for the diagnosis""")
   

   with header:
         
       st.title('DETECTING DISEASES THROUGH EYE FUNDUS IMAGE PROCESSING')
         
   with image:
      portada = Image.open('Imagenes/Collage.jpg')
      st.image(portada, use_column_width=True)
      st.subheader('Through this interface you will be able to upload an image and recieve a diagnosis for certain diseases in seconds.')

   with text:
      st.subheader('More information on eye fundus images and the models used to predict the diseases')
      st.write("""
      Eye fundus images are those obtained by reflecting light into the inside of the eye. This way you obtain a visual two dimensional representation of the retinal tissue. The interest of the eye fundus images lies in the fact that they show a very interesting part of the body, where the nervous system (via the optic nerve), the vascular system(via the capillaries feeding the nerve), and the eye meet. It is where the visual stimulus is formed, and it is a fantastic gateway into our organism and health conition.
       """)