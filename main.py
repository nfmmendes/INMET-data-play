import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#### LE DADOS 2008
df_ini = pd.read_csv("./2008/INMET_SE_MG_A552_SALINAS_01-01-2008_A_31-12-2008.CSV", sep=";",decimal=",", skiprows=8, encoding="ANSI")
df_ini = df_ini.rename({df_ini.columns[0]: 'Data'}, axis='columns')

df_ini = df_ini[["Data",\
        "HORA (UTC)",\
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]]

df_ini = df_ini.rename(columns= {"HORA (UTC)": "Hora_UTC",\
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)": "Precipitacao_Total_MM",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)": "Temperatura_Ar",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)": "Temperatura_Maxima",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)": "Temperatura_Minima"})

df_ini['Data'] = df_ini['Data'].astype('datetime64[ns]')
clean = df_ini[df_ini["Temperatura_Maxima"].between(-273, 100)]
plt.plot([ f"{x.day}/{x.month}" for x in clean["Data"]], clean["Temperatura_Maxima"].rolling(48).mean(), label="2008")


### LE DADOS 2015
df_mid = pd.read_csv("./2015/INMET_SE_MG_A552_SALINAS_01-01-2015_A_31-12-2015.CSV", sep=";",decimal=",", skiprows=8, encoding="ANSI")
df_mid = df_mid.rename({df_mid.columns[0]: 'Data'}, axis='columns')


df_mid = df_mid[["Data",\
                "HORA (UTC)",\
                "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
                "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
                "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
                "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]]

df_mid = df_mid.rename(columns= {"HORA (UTC)": "Hora_UTC",\
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)": "Precipitacao_Total_MM",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)": "Temperatura_Ar",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)": "Temperatura_Maxima",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)": "Temperatura_Minima"})


df_mid['Data'] = df_mid['Data'].astype('datetime64[ns]')
clean = df_mid[df_mid["Temperatura_Maxima"].between(-273, 100)]
#plt.plot([ f"{x.day}/{x.month}" for x in clean["Data"]], clean["Temperatura_Maxima"].rolling(48).mean(), label="2015")

### LE DADOS 2023
df_end = pd.read_csv("./2023/INMET_SE_MG_A552_SALINAS_01-01-2023_A_31-12-2023.CSV", sep=";", decimal=",", skiprows=8, encoding="ANSI")

df_end = df_end[["Data",\
        "Hora UTC", "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
        "TEMPERATURA DO PONTO DE ORVALHO (°C)",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]]

df_end = df_end.rename(columns= {"HORA (UTC)": "Hora_UTC",\
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)": "Precipitacao_Total_MM",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)": "Temperatura_Ar",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)": "Temperatura_Maxima",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)": "Temperatura_Minima"})



df_end["Data"] = df_end["Data"].astype('datetime64[ns]')
clean = df_end[df_end["Temperatura_Maxima"].between(-273, 100)]

plt.plot([f"{x.day}/{x.month}" for x in clean["Data"]], clean["Temperatura_Maxima"].rolling(48).mean(), label="2023")

plt.xticks(np.arange(0, 366, 10), rotation='vertical')
plt.legend(loc = "upper right")
plt.show()


