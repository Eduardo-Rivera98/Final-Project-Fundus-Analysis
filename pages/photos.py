import streamlit as st
import src.streamlitfunc as func


def app():
    st.title('Eye Fundus image display')
    st.write("""
    ### Here you can choose to look up an example of any of the photographs classified by diseases that we have in our dataset.
    """)
    Lista=['Choose','Diabetes','Glaucoma','Hypertension','Age Macular Degeneration','Myopia','Cataracts' ]

    enfermedad=st.selectbox ('Which disease would you like to see the porcentual distribution of?',
     Lista)
    x=str()
    if enfermedad=='Diabetes':
        x="['D']"
    elif enfermedad=='Glaucoma':
        x="['G']"
    elif enfermedad=='Hypertension':
        x="['H']"
    elif enfermedad=='Age Macular Degeneration':
        x="['A']"
    elif enfermedad=='Myopia':
        x="['M']"
    elif enfermedad=='Choose':
        st.stop()
    elif enfermedad=='Cataracts':
        x="['C']"
    func.photo(x)
        

    
    
