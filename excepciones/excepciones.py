#creando funcion que suma numeros
def sumar_dos():
    #iniciando bucle
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("Ingresa un numero")
            print(f"ERROR: {type(e).__name__}")
        #si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print("Manejo de excepciones finalizado")
    
    #mostrando el resultado
    return resultado

print(sumar_dos())