import pandas as pd

#usando la funcion read csv para leer el archivo CSV
# df = pd.read_csv("archivos\\datos.csv",names = ["name","lastname","age"]) con esta ultima opcion modificamos el nombre de las columnas

#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordenando de forma descendente
df_orden_descendente = df.sort_values("edad", ascending=False)

print(df_orden_descendente)
print(df_orden_ascendente)

#concatenando 2 dataframes 
df_concatenando = pd.concat([df,df2])

print(df_concatenando)

#accediendo a la primer fila con head()
primer_fila = df.head(2)  #el parametro que le pasamos es la cantidad de filas que queremos acceder

#accediento a las ultimas 3 dilas con tail()
ultimas_filas = df.tail(3) #la misma aclaracion que el parametro de arriba


# archivos que te van pasando y quiero hacer calculos distintos
# dependiendo la cantidad de filas y la cantidad de columnas que me pasen
# quiero saber cuantas columnas y cuantas filas hay
# porque dependiendo esta cantidad voy a hacer una cosa u otra

#accediento a la cantidad de filas y columnas con shape
filas_totales , columnas_totales = df.shape

#obteniendo data estadistica del dataframe, analisis de datos
df_info = df.describe()

print(df_info)

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

print(f"accediendo a todos los apellidos con iloc : \n{apellidos_loc}")

#accediendo a un elemento especifico del dataframe con iloc
elemente_especifico_loc = df.iloc[2,2] #accedemos a 2 = indice de la edad, 2 = indice de la columna

print(elemente_especifico_loc)

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
print(apellidos)

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]
print(fila_3)


#accediendo a filas con edad mayor a 30
mayor_que_30 = df.loc[df["edad"]>30,:]
print(f"\nAccediendo a filas con edad mayor a 30: \n{mayor_que_30}")