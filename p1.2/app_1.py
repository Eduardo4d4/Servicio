import pandas as pd               # Para la manipulación y análisis de datos
import numpy as np                # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt   # Para la generación de gráficas a partir de los datos
import seaborn as sns             # Para la visualización de datos basado en matplotlibs

BEdades = pd.read_csv('censo2020_pob_edades_alcaldia.csv')
print("DATOS SOBRE POBLACION EN ALCALDIAS \n", BEdades)
print("\n\nHola")
nameBuss = input("¿Cual es el nombre de tu negocio? \n")
alcaldia = input("Ingresa el nombre de la alcaldia donde tienes planeado establecer " + nameBuss + " \n")
sexo = input("¿Tu target debe ser Hombre o Mujer?\n")
edad = input("¿Cual es el rango de edad de tu target?\n")
groupAlcaldia = BEdades.groupby(['alcaldia', 'sexo'])
alcaldiaSelect = groupAlcaldia.get_group((alcaldia, sexo))
print("Perfeto, te presento los datos demograficos para la poblacion ", sexo, " de la alcaldia ", alcaldia)
print(alcaldiaSelect)
listaMaximo = alcaldiaSelect.loc[alcaldiaSelect['poblacion'].idxmax()]
listaSelect = alcaldiaSelect.loc[alcaldiaSelect['edad'] == edad]
maximo = listaMaximo.tolist()
seleccion = listaSelect.values.tolist()[0]
edadMax = maximo[2]
if maximo == seleccion:
    print("\n\nPerfecto, realizaste una excelecte eleccion ya que el grupo mencionado cuenta con el mayor numero de personas (", seleccion[3] ," personas ) en ", alcaldia)
    print("y por lo tanto, tinenes mas posibilidades de obtener mas clientes")
else:
    print("\n\nSeleccionaste el rango de edad ", edad, "pero este no es el que tiene mayor poblacion (", seleccion[3], " personas )")
    print("considera al grupo cuyo rango de edad es ", maximo[2], " (", maximo[3], " personas )", "ya que tiene mas posibilidades de obtener mas clientes")



"""
print("Perfecto, ahora cuentame mas sobre el target de ", nameBuss)
ingProm = input("¿Cual es el ingreso promdio del publico objetivo? (mxn) \n")
ageTarget = input("¿Cual es la edad promedio de tu publico objetivo?\n")
print("Revisemos los datos que me proporcionaste")
print("El nombre de tu empresa es ", nameBuss)
print("Con respecto a tu publico objetivo ", 
        "\nSu ingreso promedio en MXN es: ", ingProm,
        "\nSu edad promedio es: ", ageTarget
    )
    """
