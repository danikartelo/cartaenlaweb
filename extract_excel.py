import pandas as pd
CARTA = "./carta/carta.xls"

df = pd.ExcelFile(CARTA)

secs = df.sheet_names
print(secs)

for temp in secs:
    print(temp)

df = pd.read_excel(CARTA, 'entrantes')
print(str(df['nombre'][2]))
