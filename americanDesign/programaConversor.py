import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

# leer el archivo excel
df = pd.read_excel('datos.xlsx')

# anadir una columna con las pulgadas
df['pulgadas'] = df['centimetros'].apply(cm_a_pulgadas)
# apply es una función que aplica una función a cada elemento de un DataFrame

df.to_excel('datos_pulgadas.xlsx', index=False)

print("Archivo creado correctamente")