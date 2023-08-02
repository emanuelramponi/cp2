#forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados += numero
        return numeros_sumados
    
#resultado = suma([5,3,9,10,20,3])


#forma optima de sumar valores
def suma(numeros): # con args LO TENEMOS QUE PONER COMO ULTIMO PARAMETRO
    return sum([*numeros])

resultado = suma([5,3,9,10,20,3])
print(resultado)


#lo mismo que arriba pero utilizando el operador * como argumento (*args)
def suma(nombre, *numeros): # con args LO TENEMOS QUE PONER COMO ULTIMO PARAMETRO
    return f"{nombre}, la suma de tus numeros es : {sum(numeros)}"

resultado = suma("Emanuel",5,3,9,10,20,3)
print(resultado)