import os
import pandas as pd


# Leer el archivo Excel
archivo_csv = "raw_data/RPT_RG_01_Estudiantes.csv"
df = pd.read_csv(archivo_csv) 

def eliminar_columna(df):
    return df.drop(columns=['textbox19', 'SUCURSAL','textbox17','LABCIA','textbox53', 'textbox6', 'textbox145','CLISUC', 'textbox114', 'textbox111'],axis=1)

#renombrar columnas
def renombrar_columnas(df):
    return df.rename(columns={'IS_STUDENT':'ID_ESTUDIANTE',
                              'NAME_STUDENT':'NOMBRE_ESTUDIANTE',
                              'PHONE1': 'TELEFONO1',
                              'PHONE2':'TELEFONO2'})

de = eliminar_columna(df)
df = renombrar_columnas(de)

a = input("Ingrese el nombre del nuevo reporte: ")

ruta = 'normalized_data/' + a + '.xlsx'
# Crear un nuevo DataFrame con solo la columna 'Nota'
df_nueva = pd.DataFrame(df)

# Guardar el nuevo DataFrame en un nuevo archivo de Excel
df_nueva.to_excel(ruta, index=False)

print("El archivo se guardo en la ruta: ", ruta)