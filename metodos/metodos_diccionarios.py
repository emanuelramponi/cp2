#CLEAR() : Elimina todos los elementos del diccionario, dejandolo vacio
diccionario = {'a': 1, 'b': 2}
diccionario.clear()
# Resultado: {}


#GET(clave, valor_predeterminado) : Devuelve el valor asociado con la clave dada. Si la clave no esta presente en el diccionario, devueleve el valor predeterminado (o 'None' si no se proporcion)
diccionario = {'a': 1, 'b': 2}
valor = diccionario.get('b')
# Resultado: valor = 2

valor = diccionario.get('c', 0)
# Resultado: valor = 0 (clave 'c' no está presente)


#ITEMS() : Devuelve una vista iteravle de los pares clave-valor en el diccionario
diccionario = {'a': 1, 'b': 2}
pares = diccionario.items()
# Resultado: pares = [('a', 1), ('b', 2)]


#KEYS() : Devuelve una vista iterable de las claves en le diccionario
diccionario = {'a': 1, 'b': 2}
claves = diccionario.keys()
# Resultado: claves = ['a', 'b']


#VALUES() : Devuelve una vista iterable de los valores en el diccionario
diccionario = {'a': 1, 'b': 2}
valores = diccionario.values()
# Resultado: valores = [1, 2]

#POP(clva, valor_predeterminado) : Elimina y devuelve el valor asociado con la clave dada. Si la clave no esta presente en le diccionario, devuelve el valor predeterminado(o lanza un error si no se proporciona)
diccionario = {'a': 1, 'b': 2}
valor = diccionario.pop('a')
# Resultado: valor = 1, diccionario = {'b': 2}

valor = diccionario.pop('c', 0)
# Resultado: valor = 0 (clave 'c' no está presente)


#POPITEM() : Elimina y devuelve un par clave-valor aribtrario del diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
par = diccionario.popitem()
# Resultado: par = ('c', 3), diccionario = {'a': 1, 'b': 2}


#UPDATE(iterable_o_diccionario) : Actualiza el diccionario con pares clave-valor del iterable (otro diccionario o una secuencia de datos pares clave-valor)
diccionario = {'a': 1, 'b': 2}
diccionario.update({'c': 3, 'd': 4})
# Resultado: diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}



#SETDEFAULT(clave, valor_predeterminado) : Devuelve el valor asociado con la clave dada. Si la clave no esta presente en el diccionario, la agrega con el valor predeterminado (o 'None' si no se proporciona) y lo devuelve
diccionario = {'a': 1, 'b': 2}
valor = diccionario.setdefault('c', 3)
# Resultado: valor = 3, diccionario = {'a': 1, 'b': 2, 'c': 3}

valor = diccionario.setdefault('d')
# Resultado: valor = None, diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': None}
