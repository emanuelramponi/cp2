numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x: x*2

print(multiplicar_por_dos(5))

#creando una funcion comun que diga si es par o no
def es_par(num):
    if (num % 2 == 0):
        return True

#usando filtrer con una funcion comun
numeros_pares = filter(es_par,numeros)
print(f"Filter con una funcion normal : {list(numeros_pares)}")

#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero: numero % 2 == 0 ,numeros)
print(f"Filter con una funcion lambda : {list(numeros_pares)}")
