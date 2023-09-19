import streamlit as st
import ventanas as v
def main():
    st.sidebar.header('Innova UNAM')
    seleccion = st.sidebar.selectbox('Seleccione una opción',
                ('Inicio',
                'Recomendación Demografica'
                ))

    if seleccion == 'Inicio':
        v.inicio()
    if seleccion == 'Recomendación Demografica':
        v.datosDemograficos()
main()