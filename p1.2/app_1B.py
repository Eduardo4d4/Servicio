import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlibs

BEdades = pd.read_csv('censo2020_pob_edades_alcaldia.csv')
BEcono = pd.read_csv('censo2020_Caract_economicas_alcaldia.csv')
BPNEA = pd.read_csv('censo2020_PNEA_alcaldia.csv')
BEdu = pd.read_csv('censo2020_educacion_alcaldia.csv')

#print("DATOS SOBRE POBLACION EN ALCALDIAS \n", BEdades)
print("============================================================================================")
print("Hola")
"""
sexo = "hombre"
edad = "20 a 24"
print("¿Tu target debe ser Hombre o Mujer?\n", sexo)
print("¿Cuál es el rango de edad de tu target?\n", edad)
"""
sexo = input("¿Tu target debe ser Hombre o Mujer?\n")
edad = input("¿Cuál es el rango de edad de tu target?\n")

print("============================================================================================")

groupSexoEdad = BEdades.groupby(['sexo', 'edad'])
alcaldiaSelect = groupSexoEdad.get_group((sexo, edad))

top_alcaldias = alcaldiaSelect.groupby('alcaldia')['poblacion'].sum().nlargest(5)

alcaldias_list = top_alcaldias.index.tolist()

alcaldias_select = BEdades[(BEdades['alcaldia'].isin(alcaldias_list)) & (BEdades['sexo'].isin(['hombre', 'mujer']))]

total_hombres = alcaldias_select[alcaldias_select['sexo'] == 'hombre'].groupby('alcaldia')['poblacion'].sum()
total_mujeres = alcaldias_select[alcaldias_select['sexo'] == 'mujer'].groupby('alcaldia')['poblacion'].sum()

relacion_hombre_mujer = total_hombres / total_mujeres

print("Las top 5 alcaldías con mayor población para el sexo", sexo, "y edad", edad, "son:")
print(top_alcaldias)

print("\n>>Cantidad de poblacion de genero:", sexo," por cada 100 del genero opuesto<<")
print("La relación entre hombres y mujeres por alcaldías es:")
print(round(relacion_hombre_mujer, 3)* 100)


print("============================================================================================")
print("Hola 2")
"""
alcaldia = "COYOACAN"
print("¿Del top anterior, cual alcaldia le interesa conocer?\n", alcaldia)
"""
alcaldia = input("¿Del top anterior, cual alcaldia le interesa conocer?\n")

print("============================================================================================")

alcaldia_economia = BEcono[BEcono['alcaldia'] == alcaldia][['PEA','PEA_H','PEA_M','PNEA','NE']]
map_econo = {
	'PEA' : "Población económicamente activa (PEA)",
	'PEA_H' : "Porcentaje de hombres",
	'PEA_M' : "Porcentaje de mujeres",
	'PNEA' : "Población no económicamente activa (PNEA)",
	'NE' : "Población no especificada",
}

print("\nLa informacion de la poblacion economicamente activa en", alcaldia, "es:")
for columna, descripcion in map_econo.items():
    valor = alcaldia_economia[columna].values[0]
    print(f"{descripcion}: {valor}")


print("============================================================================================")

trabajo_porcentaje = BPNEA[BPNEA['alcaldia'] == alcaldia][['trabajo', 'porcentaje']]

map_trabajos = {
	'estudiante' : "Estudiante",
	'hogar' : "Personas dedicadas a los quehaceres de su hogar",
	'jubilados' : "Pensionados(as) o jubilados(as)",
	'limitados' : "Personas con alguna limitación fisica o mental que les impide trabajar",
	'otros' : "Personas en otras actividades no economicas",
}

trabajo_porcentaje['trabajo'] = trabajo_porcentaje['trabajo'].map(map_trabajos)

print("\nLa informacion de la poblacion no economicamente activa en ",alcaldia, "es:")
print(trabajo_porcentaje[['porcentaje', 'trabajo']])

print("============================================================================================")

educacion_porcentaje = BEdu[BEdu['alcaldia'] == alcaldia][['escolaridad', 'porcentaje']]

map_escolaridad = {
	'sin' : "Sin escolaridad",
	'basica' : "Básica",
	'media' : "Media superior",
	'superior' : "Superior",
	'n/e' : "No especificado",
}

educacion_porcentaje['escolaridad'] = educacion_porcentaje['escolaridad'].map(map_escolaridad)

print("\nLas características educativas de ",alcaldia, "son:")
print(educacion_porcentaje[['porcentaje', 'escolaridad']])



