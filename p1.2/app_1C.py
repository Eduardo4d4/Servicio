import pandas as pd
import tkinter as tk
from tkinter import ttk

# Función para mostrar los resultados en la interfaz gráfica
def mostrar_resultados():
    sexo = combo_sexo.get()
    edad = combo_edad.get()

    groupSexoEdad = BEdades.groupby(['sexo', 'edad'])
    alcaldiaSelect = groupSexoEdad.get_group((sexo, edad))

    top_alcaldias = alcaldiaSelect.groupby('alcaldia')['poblacion'].sum().nlargest(5)
    alcaldias_list = top_alcaldias.index.tolist()
    combo_alcaldias["values"] = alcaldias_list

# Función para mostrar la información de la alcaldía seleccionada
def mostrar_informacion_alcaldia():
    alcaldia_seleccionada = combo_alcaldias.get()

    # Mostrar la selección de alcaldía
    alcaldia_economia = BEcono[BEcono['alcaldia'] == alcaldia_seleccionada][['PEA','PEA_H','PEA_M','PNEA','NE']]
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

    label_economia.config(text=economia_text)

# Crear una ventana
window = tk.Tk()

# Configuración de la ventana
window.title("Análisis de datos")
window.geometry("400x400")

# Etiqueta y combobox para seleccionar el sexo
label_sexo = ttk.Label(window, text="¿Tu target debe ser Hombre o Mujer?")
label_sexo.pack()

combo_sexo = ttk.Combobox(window, values=["hombre", "mujer"])
combo_sexo.pack()

# Etiqueta y combobox para seleccionar el rango de edad
label_edad = ttk.Label(window, text="¿Cuál es el rango de edad de tu target?")
label_edad.pack()

combo_edad = ttk.Combobox(window, values=["0 a 4","5 a 9","10 a 14","15 a 19","20 a 24", "25 a 29", "30 a 34","35 a 39","40 a 44","45 a 49","50 a 54","55 a 59","60 a 64","65 a 69","70 a 74","75 a 79","80 a 84","85+"])
combo_edad.pack()

# Botón para mostrar los resultados
btn_mostrar = ttk.Button(window, text="Mostrar resultados", command=mostrar_resultados)
btn_mostrar.pack()

# Etiqueta para mostrar las top alcaldías
label_alcaldias = ttk.Label(window, text="")
label_alcaldias.pack()

# Combobox para seleccionar la alcaldía
label_alcaldia_seleccionada = ttk.Label(window, text="Selecciona una alcaldía:")
label_alcaldia_seleccionada.pack()

combo_alcaldias = ttk.Combobox(window)
combo_alcaldias.pack()

# Botón para mostrar la información de la alcaldía seleccionada
btn_mostrar_alcaldia = ttk.Button(window, text="Mostrar información", command=mostrar_informacion_alcaldia)
btn_mostrar_alcaldia.pack()

# Etiqueta para mostrar la información de economía
label_economia = ttk.Label(window, text="")
label_economia.pack()

# Cargar los datos
BEdades = pd.read_csv('censo2020_pob_edades_alcaldia.csv')
BEcono = pd.read_csv('censo2020_Caract_economicas_alcaldia.csv')
BPNEA = pd.read_csv('censo2020_PNEA_alcaldia.csv')
BEdu = pd.read_csv('censo2020_educacion_alcaldia.csv')

# Ejecutar la ventana
window.mainloop()

