import streamlit as st
import ventanas as v
def main():
    st.sidebar.header('Seleccione una opción')
    seleccion = st.sidebar.selectbox('Opciones',
                ('Inicio',
                'Datos Demograficos'
                ))

    if seleccion == 'Inicio':
        v.inicio()
    if seleccion == 'Datos Demograficos':
        v.datosDemograficos()
main()