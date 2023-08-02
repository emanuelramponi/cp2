def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase(adjetivo = "capo",nombre = "Ema", apellido = "Ramponi")
print(frase_resultante)

#creando la msima funcion con un parametro opcional y con un valor por defecto
def frase(nombre,apellido,adjetivo = "Imbecil"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase(nombre = "Ema", apellido = "Ramponi")
print(frase_resultante)

