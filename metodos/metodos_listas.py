# APPEND(elemento): Agrega un elemento al final de la lista
lista = [1,2,3]
lista.append(2)

print(lista)
# Resultado : [1, 2, 3, 2]


#EXTEND(iterable) : Extiende la lista agregando elementods desde un iterable
lista1 = [1,2,3]
lista2 = [4,5,6]

lista1.extend(lista2)

print(lista1)
#Resultado : [1, 2, 3, 4, 5, 6]


#INSERT(indice, elemento) : Inserta el elemento en una posicion especifica dentro de la lista

lista = [1,2,3]
lista.insert(1,100)

print(lista)
#Resultado : [1, 100, 2, 3]


#REMOVE(elemento) : Elimina la primera aparicion del elemento de la lista
lista = [1,2,3,2,3]
lista.remove(2)

print(lista)
#Resultado : [1,3,2,3]


#POP([indice]) : remove and return the element in the position given. If we do not give the index of the element is eliminate and return the last element.
lista4 = [1,2,3]
elemento =lista.pop(1)

print(lista4)
#Resultado : elemento = 2, list = [1,3] elimino el elemento del indice 1


#CLEAR(): Elimina todos los elementos de la lista, dejandola vacía.
lista = [1,2,3]
lista.clear()

#Resultado: []


#INDEX(elemento,inicio,fin) : Devuelve el indice de la primera aparicion del elemento especificado en la lista, dentro del rango opcional dado
lista = [10, 20, 30, 20, 40]
indice = lista.index(20)

print(indice)
# Resultado: indice = 1


#COUNT(elemento) : Devuelve el numero de veces que aparece el elemento en la lista.
lista = [1, 2, 3, 2, 1, 4, 1]
conteo = lista.count(1)

print(conteo)
# Resultado: conteo = 3


#SORT(key=None, reverse=False) : Ordena los elementos de la lista de forma ascendente. key and reverse son argumentos opcoonales para personalizar el ordenamiiento.
lista = [3, 1, 4, 2]
lista.sort()
# Resultado: [1, 2, 3, 4]

lista = ["manzana", "naranja", "uva"]
lista.sort(key=len)
# Resultado: ['uva', 'manzana', 'naranja']

lista = [3, 1, 4, 2]
lista.sort(reverse=True)
# Resultado: [4, 3, 2, 1]


#REVERSE() : Invierte el orden de los elementos de la lista.
lista = [1, 2, 3]
lista.reverse()
# Resultado: [3, 2, 1]




