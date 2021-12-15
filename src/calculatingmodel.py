import h5py
import cv2
from keras.models import load_model
import numpy as np
import pandas as pd
import streamlit as st

def diagnose(filepath):
    
    img = cv2.imread(filepath)
    modelMyopia = load_model("my_model_myopia.h5")
    modelGlau= load_model("my_model_glaucoma.h5")
    modelHypertension=load_model("my_model_Hypertension.h5")
    modelCataracts=load_model('modelo_bueno_cataratas.h5')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2= cv2.imread(filepath,cv2.IMREAD_COLOR)
    img2 = cv2.resize(img2, (224,224))
    img2 = img2.reshape((1,) + img2.shape)
    img2 = img2.astype(np.float32)/255
    img = cv2.resize(img, (250,250))
    img = img.astype(np.float32)/255
    img = img[..., np.newaxis]
    img = img.reshape((1,) + img.shape)
    # predict
    Myopia = (modelMyopia.predict(img))
    myopia=round(float(Myopia[0][0]),5)
    Glaucoma = (modelGlau.predict(img))
    glaucoma=round(float(Glaucoma[0][0]),5)
    Hypertension = (modelHypertension.predict(img))
    hypertension=round(float(Hypertension[0][0]),5)
    Cataracts = (modelCataracts.predict(img2))
    cataracts=round(float(Cataracts[0][0]),5)
    Enfermedades=['Myopia', 'Glaucoma', 'Hypertension', 'Cataracts']
    Porcentajes=[myopia,glaucoma,hypertension,cataracts]
    column_names = ["Disease", "Percentage"]
    dfEnfer = pd.DataFrame(columns = column_names)
    dfEnfer['Disease']=Enfermedades
    dfEnfer['Percentage']=Porcentajes
    st.dataframe(dfEnfer)