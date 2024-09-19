# Objetos tipo mapping



# Exemplo 1 - Criacao de um dicionario vazio, seguido de atribuicao de chaves e valores

dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25

# Exemplo 2 - Criacao de um dicionario com pares chave: valor

dici_2 = {'nome': "Maria", 'idade': 25}

# Exemplo 3 - Criacao de um dicionario com uma lista de tuplas representando pares chave: valor

dici_3 = dict([('nome', "Maria"), ('idade', 25)])

# Exemplo 4 - Criacao de um dicionario usando a funcao built-in zip() e duas listas, uma para 
# as chaves e outra para os valores

dici_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))


# Teste se todas as construcoes resultam em objetos iguais

print(dici_1 == dici_2 == dici_3 == dici_4) #Deve imprimir True
print(dici_1)