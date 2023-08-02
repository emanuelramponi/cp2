archivo = open("archivos\\BOCA.txt", encoding="UTF-8")

#leer archivo completo
#archivo = archivo_sin_leer.read())

#leer en una sola linea
linea = archivo.readline()

#leer linea por linea
#lineas = archivo.readlines()

#cerrar el archivo
archivo.close()

print(linea) 