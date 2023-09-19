import pandas as pd
import streamlit as st


# Cargar los datos
BEdades = pd.read_csv('censo2020_pob_edades_alcaldia.csv')
BEcono = pd.read_csv('censo2020_Caract_economicas_alcaldia.csv')
BPNEA = pd.read_csv('censo2020_PNEA_alcaldia.csv')
BEdu = pd.read_csv('censo2020_educacion_alcaldia.csv')

# Función para mostrar los resultados en la interfaz gráfica
def mostrar_resultados(combo_sexo, combo_edad):
    sexo = combo_sexo
    edad = combo_edad

    groupSexoEdad = BEdades.groupby(['sexo', 'edad'])
    alcaldiaSelect = groupSexoEdad.get_group((sexo, edad))

    top_alcaldias = alcaldiaSelect.groupby('alcaldia')['poblacion'].sum().nlargest(5)
    alcaldias_list = top_alcaldias.index.tolist()
    # Crear una cadena de texto formateada
    combo_alcaldias = "Las top 5 alcaldías con mayor población para el sexo {} y edad {} son:\n{}".format(sexo, edad, top_alcaldias)

    # Mostrar las top alcaldías
    st.text(combo_alcaldias)

    # Obtener los totales de población por género para las alcaldías seleccionadas
    alcaldias_select = BEdades[(BEdades['alcaldia'].isin(alcaldias_list)) & (BEdades['sexo'].isin(['hombre', 'mujer']))]
    total_hombres = alcaldias_select[alcaldias_select['sexo'] == 'hombre'].groupby('alcaldia')['poblacion'].sum()
    total_mujeres = alcaldias_select[alcaldias_select['sexo'] == 'mujer'].groupby('alcaldia')['poblacion'].sum()

    relacion_hombre_mujer_text = "La relación entre hombres y mujeres por alcaldía es:\n"

    if not total_hombres.empty and not total_mujeres.empty:
        relacion_hombre_mujer = total_hombres / total_mujeres
        relacion_hombre_mujer_text += relacion_hombre_mujer.reset_index().to_string(index=False, header=False)
    else:
        relacion_hombre_mujer_text += "No hay suficientes datos para calcular la relación entre hombres y mujeres."

    # Mostrar los resultados
    st.text(relacion_hombre_mujer_text)
    st.info('Cantidad hombres/mujeres por cada 100 del genero opuesto', icon="ℹ️")
    
    # return alcaldias_list
    alcaldia_selec = st.selectbox('**Top Alcaldias**', alcaldias_list)
    alcaldia_economia = BEcono[BEcono['alcaldia'] == alcaldia_selec][['PEA','PEA_H','PEA_M','PNEA','NE']]
    map_econo = {
        'PEA' : "Población económicamente activa (PEA)",
        'PEA_H' : "Porcentaje de hombres",
        'PEA_M' : "Porcentaje de mujeres",
        'PNEA' : "Población no económicamente activa (PNEA)",
        'NE' : "Población no especificada",
    }

    economia_text = ""
    for columna, descripcion in map_econo.items():
        valor = alcaldia_economia[columna].values[0]
        economia_text += f"{descripcion}: {valor} %\n"
    # Mostrar los resultados
    st.text(economia_text)
    
