import h5py
import cv2
from keras.models import load_model
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from fpdf import FPDF

def color_df(val):
    if val >= 0.6:
        color = 'red'
    elif 0.4 <val <0.6:
        color = 'orange'
    else:
        color='green'
    return f'background-color: {color}'

def diagnose(filepath,option):
    if option=='Right eye':
        img = cv2.imread(filepath)
    elif option=='Left eye':
        img=cv2.imread(filepath)
        img=cv2.flip(img,1)
    modelMyopia = load_model("my_model_myopia.h5")
    modelGlau= load_model("my_model_glaucoma.h5")
    modelHypertension=load_model("my_model_Hypertension.h5")
    modelCataracts=load_model('modelo_bueno_cataratas.h5')
    modelDiabetes=load_model('my_model_diabetes7.h5')
    modelMacular=load_model('my_model_Age_macular_degen.h5')
    modelAgePrediction=load_model('my_model_AgePrediction3.h5')
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
    Diabetes=(modelDiabetes.predict(img))
    diabetes=round(float(Diabetes[0][0]),5)
    Macular=(modelMacular.predict(img))
    macular=round(float(Macular[0][0]))
    AgePredict=(modelAgePrediction.predict(img))
    agePred=int(AgePredict)
    Enfermedades=['Myopia', 'Glaucoma', 'Hypertension', 'Cataracts','Diabetes','Age-related Macular Degeneration']
    Porcentajes=[myopia,glaucoma,hypertension,cataracts,diabetes, macular]
    column_names = ["Disease", "Percentage"]
    dfEnfer = pd.DataFrame(columns = column_names)
    dfEnfer['Disease']=Enfermedades
    dfEnfer['Percentage']=Porcentajes
    st.dataframe(dfEnfer.style.applymap(color_df, subset=['Percentage']))
    st.metric('Predicted Age', agePred)


def diagnose2(number):
    number=int(number)
    df=pd.read_csv('../full_df.csv')
    path=df.iloc[number].filename
    filepath=f'Datos/preprocessed_2/{path}'
    img = cv2.imread(filepath)
    modelMyopia = load_model("my_model_myopia.h5")
    modelGlau= load_model("my_model_glaucoma.h5")
    modelHypertension=load_model("my_model_Hypertension.h5")
    modelCataracts=load_model('modelo_bueno_cataratas.h5')
    modelDiabetes=load_model('my_model_diabetes7.h5')
    modelMacular=load_model('my_model_Age_macular_degen.h5')
    modelAgePrediction=load_model('my_model_AgePrediction3.h5')
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
    myopia=round(float(Myopia[0][0]))
    Glaucoma = (modelGlau.predict(img))
    glaucoma=round(float(Glaucoma[0][0]))
    Hypertension = (modelHypertension.predict(img))
    hypertension=round(float(Hypertension[0][0]))
    Cataracts = (modelCataracts.predict(img2))
    cataracts=round(float(Cataracts[0][0]))
    Diabetes=(modelDiabetes.predict(img))
    diabetes=round(float(Diabetes[0][0]))
    Macular=(modelMacular.predict(img))
    macular=round(float(Macular[0][0]))
    AgePredict=(modelAgePrediction.predict(img))
    agePred=int(AgePredict)
    RealAge=int(df.iloc[number]['Patient Age'])
    Enfermedades=['Myopia', 'Glaucoma', 'Hypertension', 'Cataracts','Diabetes','Age-related Macular Degeneration']
    Porcentajes=[myopia,glaucoma,hypertension,cataracts,diabetes,macular]
    Reales=[df.iloc[number].M,df.iloc[number].G, df.iloc[number].H, df.iloc[number].C, df.iloc[number].D ,df.iloc[number].A]
    column_names = ["Disease", "Probability", 'Real Values','Precision of Models']
    dfEnfer = pd.DataFrame(columns = column_names)
    dfEnfer['Disease']=Enfermedades
    dfEnfer['Probability']=Porcentajes
    dfEnfer['Real Values']= Reales
    dfEnfer['Precision of Models']=['0.82', '0.96','0.98','0.95','0.73','0.97']
    img = Image.open(filepath)
    st.image(img)
    st.dataframe(dfEnfer.style.applymap(color_df, subset=['Probability']))
    st.metric('Predicted Age', agePred)
    st.metric('Real Age',RealAge)


    def perro(filepath,option):
        if option=='Right eye':
            img = cv2.imread(filepath)
        elif option=='Left eye':
            img=cv2.imread(filepath)
            img=cv2.flip(img,1)
        modelMyopia = load_model("my_model_myopia.h5")
        modelGlau= load_model("my_model_glaucoma.h5")
        modelHypertension=load_model("my_model_Hypertension.h5")
        modelCataracts=load_model('modelo_bueno_cataratas.h5')
        modelDiabetes=load_model('my_model_diabetes7.h5')
        modelMacular=load_model('my_model_Age_macular_degen.h5')
        modelAgePrediction=load_model('my_model_AgePrediction3.h5')
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
        Diabetes=(modelDiabetes.predict(img))
        diabetes=round(float(Diabetes[0][0]),5)
        Macular=(modelMacular.predict(img))
        macular=round(float(Macular[0][0]))
        AgePredict=(modelAgePrediction.predict(img))
        agePred=int(AgePredict)
        Porcentajes=[myopia,glaucoma,hypertension,cataracts,diabetes,macular]
        Lista=[]
        for i in Porcentajes:
            if i == 1:
                Lista.append('Positive')
            else:
                Lista.append('Negative')
        return f""" 
        * Myopia = {Lista[0]}
        * Glaucoma = {Lista[1]}
        * Hypertension = {Lista[2]}
        * Cataracts = {Lista[3]}
        * Diabetes= {Lista[4]}
        * Age-related Macular Degeneration = {Lista[5]}
        * Yor eye has the age of a {agePred} year old
        """
        
def create_PDF(name, email, path,option):
    '''
    Given a name, email, xray date and xray file path, generates PDF
    with a Pneumonia diagnosis
    Takes: name, email, xray date and xray file path
    Returns: path for PDF with Pneumonia diagnosis
    '''

    # create pdf object with default params
    pdf = FPDF()

    # add a page to start "writing"
    pdf.add_page()

    # length and width of A4 page
    # pdf_w=210
    # pdf_h=297

    # draw two rectangles as a margin and fill with grey
    pdf.set_fill_color(128, 128, 128) # RGB
    
    pdf.rect(5.0, 5.0, 200.0,287.0, "DF") # abscissa upper left corner, ordinate top left, rec width, rec height, fill style
    pdf.set_fill_color(255, 255, 255)

    pdf.rect(8.0, 8.0, 194.0,282.0, "FD")

    # insert logo on top right corner
    pdf.set_xy(175.0,12.0)
    pdf.image('Imagenes/Collage.jpg', w=20.0)
    
    # add title
    pdf.set_xy(100.0,20.0)
    pdf.set_font('Arial', 'B', 16) # family, style, size
    pdf.set_text_color(0, 0, 50) # RGB
    pdf.cell(w=5.0, h=40.0, align='C', txt="EYE FUNDUS DIAGNOSIS", border=0)
    
    # insert x-ray image
    pdf.set_xy(20.0,135.0)
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(64,64,64)
    pdf.cell(173, 8, "Patient's Eye-Fundus", border = 1)
    
    pdf.set_xy(42.5,160.0)
    pdf.image(path, w=120.0)
    
    # inset text comments
    pdf.set_xy(20.0,50.0)
    pdf.set_font("Arial", "U", 12)
    pdf.set_text_color(64,64,64)

    diagnosis = perro(path,option)
    pdf.cell(30, 15, f"Patient name:")
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(30, 15, f"{name}", ln = 1)

    pdf.set_xy(20.0,65.0)
    pdf.set_font("Arial", "U", 12)
    pdf.cell(30, 15, f"Patient email:")
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(30, 15, f"{email}", ln = 1)

    
    pdf.set_xy(20.0,105.0)
    pdf.cell(30, 15, f"Your eye fundus analysis presents the following results: {diagnosis} ")
    
    # save file
    save_path = f"PDFs/{name} - {option}"
    pdf.output(save_path, "F")

    return save_path