import pandas as pd
print(type(pd))

with open("archivos\\BOCA.txt",'a',encoding="UTF-8") as archivo:
    archivo.write("\n")
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")