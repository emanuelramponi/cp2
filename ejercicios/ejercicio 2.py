#falto elprofe y los pibes van a armar la clase

#peir el nombre y la edad de los compa;eros que vinieron hoy a clas

#funcion para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista de los compañeros
    compañeros = []
    
    for i in range(cantidad_de_compañeros):
        
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
    
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
#ordenando los de menor a mayor segun su edad
    compañeros.sort(key = lambda x:x[1])

    #compañeros[x] devuelve una tupla con nombre y edad, y despues ccedemos al nombre para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

print(f"El profesor es {profesor} y su asistente es {asistente}")


