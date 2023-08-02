# listas, una con nombre otra con apellidos
nombre = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Daltp","Rodriguez","Coto"]

# Registrar esta informacion en un TXT en forma optima

with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------------\n)" for n,a in zip(nombre,apellidos))]
    
    