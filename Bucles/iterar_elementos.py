animales = ["pez","gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72,34]

#recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a : {animal}")
    
#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(f"{numero} * {10} : {numero*10}")

#zip() iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(numeros, animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")    


#range() 
for num in range(10,234):
    print(num)
    
#forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0] #con el indice 0 nos va a indicar en que numero de indice esta
    valor = num[1]
    print(f"el indice es : {indice}  y el valor es: {valor}")
    print(num)
    

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino") #el else despues del for siempre se va a ejecutar. Solamente una vez al final del bucle
    


#TODO LO ANTERIOR FUNCIONA EXACTAMENTE IGUAL PARA TUPLAS y CONJUNTOS