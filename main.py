import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = open("files.txt", "r")
file_content = file.read()
file_list = file_content.splitlines() #[ x.split('\n') for x in file_list ]
file_list_splitted = [ x.strip().split('_')[0 : 8] for x in file_list if len(x) > 2]
print(file_list_splitted[0])
df_files = pd.DataFrame(columns=["INMET", "REGIAO", "ESTADO", "CODIGO", "CIDADE", "DATA INI", "A", "DATA FIM"],
                        data = file_list_splitted).drop(columns={"INMET", "A"})

#### LE DADOS 2008
df_ini = pd.read_csv("./2008/INMET_SE_MG_A552_SALINAS_01-01-2008_A_31-12-2008.CSV", sep=";",decimal=",", skiprows=8, encoding="ANSI")
df_ini = df_ini.rename({df_ini.columns[0]: 'Data'}, axis='columns')


selected_cols = [df_ini.columns[0], df_ini.columns[1],\
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]

df_ini = df_ini[selected_cols].rename(columns= {\
        selected_cols[1]: "Hora_UTC",\
        selected_cols[2]: "Precipitacao_Total_MM",\
        selected_cols[3]: "Temperatura_Ar",\
        selected_cols[4]: "Temperatura_Maxima",\
        selected_cols[5]: "Temperatura_Minima"})

df_ini['Data'] = df_ini['Data'].astype('datetime64[ns]')
clean = df_ini[df_ini["Temperatura_Maxima"].between(-273, 100)]
plt.plot([ f"{x.day}/{x.month}" for x in clean["Data"]], clean["Temperatura_Maxima"].rolling(48).mean(), label="2008")


### LE DADOS 2015
df_mid = pd.read_csv("./2015/INMET_SE_MG_A552_SALINAS_01-01-2015_A_31-12-2015.CSV", sep=";",decimal=",", skiprows=8, encoding="ANSI")

selected_cols[0] = df_mid.columns[0]
df_mid = df_mid[selected_cols].rename(columns= {\
        selected_cols[0]: "Data",\
        selected_cols[1]: "Hora_UTC",\
        selected_cols[2]: "Precipitacao_Total_MM",\
        selected_cols[3]: "Temperatura_Ar",\
        selected_cols[4]: "Temperatura_Maxima",\
        selected_cols[5]: "Temperatura_Minima"})

df_mid['Data'] = df_mid['Data'].astype('datetime64[ns]')
clean = df_mid[df_mid["Temperatura_Maxima"].between(-273, 100)]
#plt.plot([ f"{x.day}/{x.month}" for x in clean["Data"]], clean["Temperatura_Maxima"].rolling(48).mean(), label="2015")

### LE DADOS 2023
df_end = pd.read_csv("./2023/INMET_SE_MG_A552_SALINAS_01-01-2023_A_31-12-2023.CSV", sep=";", decimal=",", skiprows=8, encoding="ANSI")

selected_cols[0] = df_end.columns[0]
selected_cols[1] = df_end.columns[1]

df_end = df_end[selected_cols].rename(columns= {\
        selected_cols[0]: "Data",\
        selected_cols[1]: "Hora_UTC",\
        selected_cols[2]: "Precipitacao_Total_MM",\
        selected_cols[3]: "Temperatura_Ar",\
        selected_cols[4]: "Temperatura_Maxima",\
        selected_cols[5]: "Temperatura_Minima"})


df_end["Data"] = df_end["Data"].astype('datetime64[ns]')
clean = df_end[df_end["Temperatura_Maxima"].between(-273, 100)]

plt.plot([f"{x.day}/{x.month}" for x in clean["Data"]], clean["Temperatura_Maxima"].rolling(48).mean(), label="2023")

plt.xticks(np.arange(0, 366, 10), rotation='vertical')
plt.legend(loc = "upper right")
plt.show()


