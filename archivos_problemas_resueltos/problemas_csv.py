#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
# print(type(df['edad'][0]))

#reemplazando los datos "dalto" por "Maestro"
df['edad'].replace("dalto","maestro",inplace=True)

#eliminando las filas con datos vacios
print(df)
#si quiero eliminar la columna es df ) df.dropna(axis=1)
print("\nEliminando datos vacios\n")
df = df.dropna()
print(f"{df} \n")

#eliminamos las filas repetidas
print("\nEliminando datos repetidos\n")
df = df.drop_duplicates()
print(df)


#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")