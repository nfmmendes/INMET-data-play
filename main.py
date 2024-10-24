import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#### LE DADOS 2008
df_ini = pd.read_csv("./2008/INMET_SE_MG_A552_SALINAS_01-01-2008_A_31-12-2008.CSV", sep=";",decimal=",", skiprows=8, encoding="ANSI")


df_ini = df_ini[["DATA (YYYY-MM-DD)",\
        "HORA (UTC)",\
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]]

df_ini['DATA (YYYY-MM-DD)'] = df_ini['DATA (YYYY-MM-DD)'].astype('datetime64[ns]')
clean = df_ini[df_ini["TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)"].between(-273, 100)]
plt.plot([ f"{x.day}/{x.month}" for x in clean["DATA (YYYY-MM-DD)"]], clean["TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)"].rolling(48).mean(), label="2008")


### LE DADOS 2015
df_mid = pd.read_csv("./2015/INMET_SE_MG_A552_SALINAS_01-01-2015_A_31-12-2015.CSV", sep=";",decimal=",", skiprows=8, encoding="ANSI")

df_mid = df_mid[["DATA (YYYY-MM-DD)",\
                "HORA (UTC)",\
                "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
                "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
                "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
                "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]]

df_mid['DATA (YYYY-MM-DD)'] = df_mid['DATA (YYYY-MM-DD)'].astype('datetime64[ns]')
clean = df_mid[df_mid["TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)"].between(-273, 100)]
#plt.plot([ f"{x.day}/{x.month}" for x in clean["DATA (YYYY-MM-DD)"]], clean["TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)"].rolling(48).mean(), label="2015")

### LE DADOS 2023
df_end = pd.read_csv("./2023/INMET_SE_MG_A552_SALINAS_01-01-2023_A_31-12-2023.CSV", sep=";", decimal=",", skiprows=8, encoding="ANSI")

df_end = df_end[["Data",\
        "Hora UTC", "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)",\
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)",\
        "TEMPERATURA DO PONTO DE ORVALHO (°C)",\
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)",\
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)"]]


df_end["Data"] = df_end["Data"].astype('datetime64[ns]')
clean = df_end[df_end["TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)"].between(-273, 100)]

plt.plot([f"{x.day}/{x.month}" for x in clean["Data"]], clean["TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)"].rolling(48).mean(), label="2023")

print(len(clean))
plt.xticks(np.arange(0, 366, 10), rotation='vertical')
plt.legend(loc = "upper right")
plt.show()


