import pandas as pd

# Criando uma DataFrame com 5 linhas de dados
data = {
    'nome':['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
    'quantidade de itens comprados':[3, 1, 4, 3, 2],
    'tipo de item':['Eletronico', 'Vestuario', 'Alimento', 'Eletronico', 'Alimento'],
    'receita total':[120, 80, 60, 120, 90]
}

df = pd.DataFrame(data)

# Duplicando uma linha
df.drop_duplicates(keep='last', inplace=True)

# Calculando a coluna 'preco do item'
df['preco do item'] = df['receita total'] / df['quantidade de itens comprados']

# Selecionando preco do item acima de 50 reais
itens_acima_de_50 = df[df['preco do item']>50]

print("Itens acima de 50 reais:")
print(itens_acima_de_50)