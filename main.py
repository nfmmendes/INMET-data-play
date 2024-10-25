import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

file = open("files.txt", "r")
file_content = file.read()
file_list = [x for x in file_content.splitlines() if len(x) > 2]
file_list_splitted = [ x.replace(".CSV","").strip().split('_')[0 : 8] + [x] for x in file_list]

df_files = pd.DataFrame(columns=["INMET", "REGIAO", "ESTADO", "CODIGO", "CIDADE", "DATA INI", "A", "DATA FIM", "ARQUIVO"],
                        data = file_list_splitted).drop(columns={"INMET", "A"})
df_files["ANO"] = df_files["DATA FIM"].apply(lambda x: x.split('-')[-1])
print(df_files)
print(f"Existem dados de {len(df_files['CIDADE'].unique())} cidades")


cidade = "SALINAS"
df_cidade = df_files[df_files['CIDADE'] == cidade][['ARQUIVO','ANO']]


fig, ax = plt.subplots()

for i in range(0, len(df_cidade)):
    file_name = df_cidade.iloc[i]['ARQUIVO']
    pasta = df_cidade.iloc[i]['ANO']
    df = pd.read_csv(f"./{pasta}/{file_name}", sep=";", decimal=',', skiprows=8, encoding="ANSI")

    selected_cols = [df.columns[0], df.columns[1],\
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]

    df = df[selected_cols].rename(columns= {\
        selected_cols[0]: "Data",\
        selected_cols[1]: "Hora_UTC",\
        selected_cols[2]: "Precipitacao_Total_MM",\
        selected_cols[3]: "Temperatura_Ar",\
        selected_cols[4]: "Temperatura_Maxima",\
        selected_cols[5]: "Temperatura_Minima"})

    df['Data'] = df['Data'].astype('datetime64[ns]')
    df = df.sort_values(by='Data')
    df = df.groupby(by='Data').agg({'Hora_UTC': 'last',\
                                    'Precipitacao_Total_MM': 'sum',\
                                    'Temperatura_Ar': 'mean',\
                                    'Temperatura_Maxima': 'mean',\
                                    'Temperatura_Minima': 'mean',\
                                     })
    
    clean = df[df["Temperatura_Maxima"].between(-273, 100)]
    
    x_values = [ x.timetuple().tm_yday for x in clean.index]
    plt.plot(x_values, clean["Temperatura_Maxima"], label=pasta)

labels = [datetime.strptime("2024-" + str(day_num), "%Y-%j").strftime("%m-%d") for day_num in np.arange(1, 367, 10) ]
ax.set_xticklabels(labels)
plt.xticks(np.arange(0, 366, 10), rotation='vertical')
plt.legend(loc = "upper right")
plt.show()


