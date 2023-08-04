import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\bigotes.csv")

#creando el grafico
sns.boxplot(x= "categoria", y = "valor", data = df)

#mostrando el grafico
plt.show()


def read_csv_in_chunks(file_name):
    for i, chunk in enumerate(pd.read_csv(file_name, chunksize=1000)):
        print("Chunk #{}".format(i))
        print(chunk)

read_csv_in_chunks("archivs_problemas_graficos\\dispersion_file.csv")