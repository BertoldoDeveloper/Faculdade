# Podemos usar a biblioteca pandas para descobrir em qual público a loja deve investir.
# Para tanto, devemos calcular a média de idade dos clientes.

import pandas as pd

# Criando um dicionario com nomes e idades
dados = {
    'Nome': ['Alice', 'Bob', 'Pedro', 'Andressa', 'Ladislau', 'Daniela'],
    'Idade': [25, 30, 18, 27, 27, 31]
}

# Criando uma serie a partir do dicionario 
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])

# Exivindo a serie de idades
print("Serie de Idades:")
print(serie_idades)

# Calculando a media das idades
media_idades = serie_idades.mean()

print("\nMedia de Idades:", (int(media_idades)))
