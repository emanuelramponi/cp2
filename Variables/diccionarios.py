#creando diccionarios con dict()

diccionario = dict(Nombre = "emanuel", apellido = "ramponi") #para crear diccionarios vacios solamente es con esta funcion, al igual que las listas y tupas


print(diccionario) 

#las tuplas pueden ser claves
diccionarios = {("marvel","thor"): "thunder"}
print(diccionarios)

#pero las listas NO pueden ser claves
#diccionarios = {["marvel","thor"]: "thunder"}
diccionarios = {frozenset(["marvel","thor"]): "thunder"}
print(diccionarios)


#y tampoco los conjuntos pueden ser claves
#diccionarios = {{"marvel","thor"}: "thunder"} 
#print(diccionarios) unhasheable |


#creando diccionarios con fromkeys, con valores None, sin asignar
diccionarios = dict.fromkeys(["nombre","apellido","suscriptores"],"vacio") #el primer valor es el iterable, y el segundo es el que vamos a igualar.
print(diccionarios)