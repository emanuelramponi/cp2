nombre = 'Mario'

bienvenido = f"Bienvenido {nombre} ¿Como estas?"

# (del nombre) eliminamos datos que se alojaron en la memoria



# DATOS COMPUESTOS 

#creando una lista (se pueden modificar)
lista = ["A", "B", "C", "D", "E",True,1.64]

#creando una tupla (no se pueden modificar)
tupla = ("A", "B", "C", "D", "E",True,1.64)

#esto es validdo
lista[3] = "Aguante Boca"

#esto no
#tupla[3] = "Aguante Boca"


#creando un conjunot(set)
conjunto = {"A","b","c","d","e","f","g",True,21.2} #son elementos desordenados que se pueden modificar, pero no se pueden modificar elementos al igual que las tuplas
                                                    #se puede redefinir pero no modificar
                                                    #no podemos acceder al set por el indice del elemento
                                                    #NO ALMACENA DATOS DESORDENADOS
                                                    
#creando un diccionario 
diccionario = {
    'Nombre': "Emanuel",
    'Apellido': "Ramponi",
    'Edad' : 20,
    'esta_emocionado': True
}

print(diccionario['Apellido'])


