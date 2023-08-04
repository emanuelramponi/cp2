import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv_in_chunks(file_name):
    for i, chunk in enumerate(pd.read_csv(file_name, chunksize=1000)):
        print("Chunk #{}".format(i))
        print(chunk)

read_csv_in_chunks("archivos_problemas_graficos\\dispersion.csv")