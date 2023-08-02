#crear una funcion que nos retorne multiples valores
def crear_password_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return password, num


#desempaquetando la funcion
password, primer_numero = crear_password_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es : {password}")
print(f"El numero utilizado para crearla fue : {primer_numero}")

