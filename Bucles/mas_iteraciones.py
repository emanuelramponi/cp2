#creamos las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "BOCAAAAA"
numeros = [2,5,8,10]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f"Me voy a comer una {fruta}")
    
#evitar que el bulce siga ejectuandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == 'pera':
        break
else:
    print("terminado") #con el BREAK NO se ejecuta el else
    
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)