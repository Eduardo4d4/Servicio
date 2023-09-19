import streamlit as st
from PIL import Image
from datetime import datetime
import demo as d

def inicio():
    logo_unam = Image.open('img/unam.png')
    logo_fi = Image.open('img/FI.png')
    logo_innova = Image.open('img/innova.png')
    logo_innova_BT = Image.open('img/innova_BT.png')
    
    # Fecha de la última actualización -cuando se inicia la aplicación-
    fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.image(logo_innova)
    with st.container():
        col1, col2 = st.columns([1, 4])   
        with col1:
            st.write(" ")
            st.write(" ")
            st.image(logo_innova_BT, width=100)
        with col2:    
            st.write(" ")
            st.write('<h4 style="text-align: center;">Base Tecnologica</h4>', unsafe_allow_html=True)
            st.markdown('<h5 style="text-align: center;">Empresas dedicadas a bienes y/p servicios derivados de conocimiento nuevo usualmente generado en la Universidad, sujeto al licenciamiento o transferencia de sus derechos de propiedad</h5>', unsafe_allow_html=True)
    
    st.divider()
    with st.container():
        st.markdown("**Proyecto:** _Recomendación Demografica_ ")
        st.markdown("Nuestro propósito es ofrecer a emprendedores y empresas una herramienta confiable que, mediante análisis de datos demográficos y geográficos, identifique ubicaciones estratégicas para sus negocios, optimizando su potencial de éxito.")
        st.info("La información proporcionada será manejada con confidencialidad y solo será utilizada con el propósito de optimizar nuestros servicios en beneficio de su negocio.", icon="ℹ️")

    st.divider()
    with st.container():
        col1, col2, col3 = st.columns([4, 1, 1])   
        with col1:
            st.markdown('<h5 style="text-align: center;">Proyecto: "Recomendación Demografica"</h5>', unsafe_allow_html=True)
            st.markdown('<h6 style="text-align: center;">Innova UNAM - FI</h6>', unsafe_allow_html=True)
            # Mostrar la fecha de la última actualización en la interfaz
            st.write(":blue[Fecha de última actualización:]", fecha_actualizacion)
        with col2:
                st.image(logo_unam, width=80)  
        with col3: 
                st.image(logo_fi, width=80)     

            
   

def datosDemograficos():
    logo_unam = Image.open('img/unam.png')
    logo_fi = Image.open('img/FI.png')
    col1, col2, col3 = st.columns([1, 4, 1])   
    with col1:
        st.image(logo_unam, width=80)  
    with col2:
        st.markdown('<h1 style="text-align: center;">Analisis de datos</h1>', unsafe_allow_html=True)
    with col3:
        st.image(logo_fi, width=80)  
    
    st.success("Por favor, complete todos los campos relacionados con su público objetivo.", icon="✅")
    combo_sexo = st.radio('Sexo preferente del target:', ["hombre", "mujer"])
    combo_edad = st.selectbox('Rango de edad del target:',
                ("0 a 4","5 a 9","10 a 14","15 a 19","20 a 24", "25 a 29", "30 a 34","35 a 39","40 a 44","45 a 49","50 a 54","55 a 59","60 a 64","65 a 69","70 a 74","75 a 79","80 a 84","85+"
                ))
    st.divider()
    if st.checkbox('Mostrar resultados'):
        d.mostrar_resultados(combo_sexo, combo_edad)

            
            


