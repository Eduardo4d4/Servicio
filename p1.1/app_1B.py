import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlibs

BEdades = pd.read_csv('censo2020_pob_edades_alcaldia.csv')
#print("DATOS SOBRE POBLACION EN ALCALDIAS \n", BEdades)
print("============================================================================================")
print("Hola")
sexo = "hombre"
edad = "20 a 24"
print("¿Tu target debe ser Hombre o Mujer?\n", sexo)
print("¿Cuál es el rango de edad de tu target?\n", edad)
"""
sexo = input("¿Tu target debe ser Hombre o Mujer?\n")
edad = input("¿Cuál es el rango de edad de tu target?\n")
"""
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
"""
print("\nEl total de hombres por alcaldía en estas alcaldías es:")
print(total_hombres)
print("\nEl total de mujeres por alcaldía en estas alcaldías es:")
print(total_mujeres)
"""
print("\n>>Cantidad de poblacion de genero:", sexo," por cada 100 del genero opuesto<<")
print("La relación entre hombres y mujeres por alcaldías es:")
print(round(relacion_hombre_mujer, 3)* 100)

