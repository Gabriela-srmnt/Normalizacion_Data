import os
import pandas as pd


# Leer el archivo Excel
archivo_csv = "raw_data/RPT_RM_03_EstudiantesNiveles.csv"
df = pd.read_csv(archivo_csv) 

def eliminar_columna(df):
    return df.drop(columns=['Textbox73', 'Textbox78','Textbox79','Textbox74'], axis=1)

#renombrar columnas
def renombrar_columnas(df):
    return df.rename(columns={'CLINAM2':'NOMBRE_ESTUDIANTE',
                              'GRPCUN2':'ID_ESTUDIANTE',
                              'Textbox75': 'IDENTIFICACION',
                              'Textbox76':'TOTAL_CREDITO_CUATRI',
                              'ESCUELA2':'ESCUELA',
                              'ENFASIS2':'ENFASIS',
                              'Textbox77':'TOTAL_ACUMULADO_CUATRIMESTRE',
                              'CLIPAI2':'NACIONALIDAD',
                              'CARCOD2':'GENERO',
                              'CARCOD3':'EDAD',
                              'CLIEM2':'EMAIL',
                              'CLITCE2':'TELEFONO1',})

de = eliminar_columna(df)
df = renombrar_columnas(de)

a = input("Ingrese el nombre del nuevo reporte: ")

ruta = 'normalized_data/' + a + '.xlsx'
# Crear un nuevo DataFrame con solo la columna 'Nota'
df_nueva = pd.DataFrame(df)

# Guardar el nuevo DataFrame en un nuevo archivo de Excel
df_nueva.to_excel(ruta, index=False)

print("El archivo se guardo en la ruta: ", ruta)