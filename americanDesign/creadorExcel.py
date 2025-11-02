import pandas as pd

data = {
    'elementos': ['mesa', 'silla', 'cama', 'armario', 'tv', 'sofa', 'escritorio', 'lampara', 'jarron', 'escultura'],
    'centimetros': [100, 50, 200, 150, 80, 120, 100, 50, 30, 100],
}

df = pd.DataFrame(data)

df.to_excel('datos.xlsx', index=False)
