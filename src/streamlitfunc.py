import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib as plt
import cv2
from PIL import Image

def crear_visualizacion(x ,enfermedad):
    df=pd.read_csv('../full_df.csv')
    dfunicos=df.drop_duplicates(subset='ID')
    IDunicos=dfunicos.ID
    IDenfermedades=df.loc[(df[f'{x}'] == 1)]['ID'].values
    IDunicoenfermedades=set(IDenfermedades)
    ListaIDenfer=list(IDunicoenfermedades)
    ListaIDnoenfer=[]
    for i in IDunicos:
        if i not in ListaIDenfer:
            ListaIDnoenfer.append(i)
    AgeEnfer=[]
    for i in ListaIDenfer:
        c=dfunicos.loc[dfunicos.ID==i]['Patient Age'].values
        c=int(c)
        AgeEnfer.append(c)
    AgeNoEnfer=[]
    for i in ListaIDnoenfer:
        c=dfunicos.loc[dfunicos.ID==i]['Patient Age'].values
        c=int(c)
        AgeNoEnfer.append(c)
    column_names = ["ID", "Age", f"{enfermedad}"]
    dfEnfer = pd.DataFrame(columns = column_names)
    dfNoEnfer=pd.DataFrame(columns=column_names)
    dfNoEnfer.ID=ListaIDnoenfer
    dfNoEnfer.Age=AgeNoEnfer
    dfNoEnfer[f'{enfermedad}']=0
    dfEnfer.ID=ListaIDenfer
    dfEnfer.Age=AgeEnfer
    dfEnfer[f'{enfermedad}']=1
    dfenfermedad=pd.concat([dfEnfer,dfNoEnfer])
    dfenfermedad['Ageinterval']=pd.cut(dfenfermedad.Age, 10)
    c=dfenfermedad.groupby(['Ageinterval']).agg({f'{enfermedad}':'mean'})
    c.reset_index(inplace=True)
    Ages=[]
    for i in c.Ageinterval:
        e=i.mid
        Ages.append(e)
    c['Ages']=Ages
    fig = px.histogram(c,x=c.Ageinterval.astype('str'), y=c[f'{enfermedad}'],nbins=10, color='Ageinterval')
    fig.update_layout(title={"text": f"{enfermedad} Distribution"},xaxis_title='Age', yaxis_title=f"Percentage of {enfermedad}")
    st.plotly_chart(fig)

def photo(x):
    df=pd.read_csv('../full_df.csv')
    seg = df[df['labels']==x]
    filename = seg.sample().iloc[0]['filename']
    fulladdress=f'Datos/preprocessed_2/{filename}'
    img = Image.open(fulladdress)
    st.image(img)


    