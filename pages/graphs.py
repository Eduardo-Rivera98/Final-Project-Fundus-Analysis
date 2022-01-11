import streamlit as st
import src.streamlitfunc as graf
from PIL import Image
def app():
    st.header('Graphs & Visualizations')
    image = Image.open("Imagenes/Collage2.jpg")
    st.image(image)
    Distribucion=st.container()
    info=st.expander('More information about these graphs')
    Matriz=st.container()
    info2=st.expander('More information about confusion matrixes')
    with Distribucion:
        st.subheader("""Data distribution Graphs
        """)
        Lista=['Choose','Diabetes','Glaucoma','Hypertension','Age Macular Degeneration','Myopia','Cataracts' ]

        enfermedad=st.selectbox ('Which disease would you like to see the porcentual distribution of?',
        Lista)
        if enfermedad !='Choose':
            x=str()
            if enfermedad=='Diabetes':
                x='D'
            elif enfermedad=='Glaucoma':
                x='G'
            elif enfermedad=='Hypertension':
                x='H'
            elif enfermedad=='Age Macular Degeneration':
                x='A'
            elif enfermedad=='Myopia':
                x='M'
            elif enfermedad=='Cataracts':
                x='C'
            graf.crear_visualizacion(x,enfermedad)
    with info:
        st.write(""" This graph shows the percentaje of people within each age group of our dataset that has been diagnosed with the selected disease. """)
    with Matriz:
        st.subheader('Confusion Matrix of the models')
        Lista2=['Choose','Diabetes','Glaucoma','Hypertension','Age Macular Degeneration','Myopia','Cataracts' ]
        modelo=st.selectbox('Which model would you like to see the confusion matrix of?', Lista2)
        if modelo !='Choose':
            z=str()
            if modelo=='Diabetes':
                z='Matriz_Diabetes.png'
            elif modelo=='Glaucoma':
                z='Matriz_Glaucoma.png'
            elif modelo=='Hypertension':
                z='Matriz_Hypertension.png'
            elif modelo=='Age Macular Degeneration':
                z='Matriz_Macular_degen.png'
            elif modelo=='Myopia':
                z='Matriz_Myopia.png'
            elif modelo=='Cataracts':
                z='Matriz_Cataratas.png'
            graf.matriz(z)
    
    with info2:
        st.write('A confusion matrix is a performance measurement for machine learning classification problem where output can be two or more classes. It is a table with 4 different combinations of predicted and actual values.')
        imagen=Image.open('Imagenes/confusion.png')
        st.image(imagen,width=500)