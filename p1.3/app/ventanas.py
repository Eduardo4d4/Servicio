import streamlit as st
from PIL import Image
import demo as d

def inicio():
    image1 = Image.open('img/unam.png')
    image2 = Image.open('img/FI.png')
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        with st.container():
            st.image(image1, width=100)
    with col2:
        st.markdown('<h3 style="text-align: center;">Proyecto</h3>', unsafe_allow_html=True)
        st.markdown('<h3 style="text-align: center;">Recomendación de negocios</h3>', unsafe_allow_html=True)
        st.markdown('<h4 style="text-align: center;">Innova FI</h4>', unsafe_allow_html=True)
        st.markdown('<p>Favor de llenar...</p>', unsafe_allow_html=True)
    with col3:
        with st.container():
            st.image(image2, width=100)

def datosDemograficos():
    st.markdown('<h1 style="text-align: center;">Analisis de datos</h1>', unsafe_allow_html=True)
    st.markdown('<p>"¿Tu target debe ser Hombre o Mujer?"</p>', unsafe_allow_html=True)
    opciones = ["hombre", "mujer"]
    combo_sexo = st.radio('Selecciona una opción:', opciones)
    combo_edad = st.selectbox('Rangos de edad',
                ("0 a 4","5 a 9","10 a 14","15 a 19","20 a 24", "25 a 29", "30 a 34","35 a 39","40 a 44","45 a 49","50 a 54","55 a 59","60 a 64","65 a 69","70 a 74","75 a 79","80 a 84","85+"
                ))
    if st.button('Mostrar resultados'):
        combo_alcaldias = d.mostrar_resultados(combo_sexo, combo_edad)
        st.markdown('<p>Selecciona una alcaldia</p>', unsafe_allow_html=True)
        alcaldia_selec = st.selectbox('Top Alcaldias',combo_alcaldias)
        if alcaldia_selec == True:
            d.mostrar_informacion_alcaldia(alcaldia_selec)
            
            


