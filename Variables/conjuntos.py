#creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset(["Dato 1", "Dato 2"]) #frozenset = crea un conjunto inmutable para poder ser hasheado y agregar otro conjunto dentro de otro conjunto
conjunto2 = {conjunto1, "Dato 3"}

#TEORIA DE CONJUNTOS
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1)
resultado = conjunto1 <= conjunto2
#estas son 2 formas de verificar si es un subconjunto
print(resultado)

#verifcando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto1 > conjunto1
print(resultado)

#verificamos si hay algun elemento en comun
resultado = conjunto2.isdisjoint(conjunto1)
#con que haya un elemento que sea igual, el resultado va a ser false. Va a ser true solamente cuando los conjuntos que se estan comparando no tienen ningun valor igual

print(resultado)

