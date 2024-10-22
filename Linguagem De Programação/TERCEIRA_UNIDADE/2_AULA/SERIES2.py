import pandas as pd

# Criando um dicionario para pares chave-valor
data = {'A':100, 'B':200, 'C':300, 'D':400, 'E':500}

# Criando uma Series a partir do dicionario
series2 = pd.Series(data)

print(series2)