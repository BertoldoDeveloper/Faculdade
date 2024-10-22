# Vamos, agora, colocar em prática o que aprendemos pensando no problema apresentado 
# no início desta aula. Cada venda é registrada como uma tupla com os seguintes elementos:
# data da venda, nome do produto, quantidade vendida e preço unitário. Essas tuplas são 
# armazenadas em uma lista chamada registros_de_vendas. Além disso, você recebeu uma lista 
# de produtos que precisam ser reabastecidos no estoque, chamada produtos_a_reabastecer. 
# Também é preciso acompanhar o total de vendas de cada produto. Para fazer isso, você deve 
# criar um dicionário chamado total_de_vendas_por_produto, no qual as chaves são os nomes 
# dos produtos, e os valores são os totais de vendas para cada um.



# tupla de convidados
convidados = ("Alice", "Bob", "Carol", "Junior", "Eve")

# Lista de confirmados
confirmados = ["Bob", "Junior", "Carol"]

# Identificar quem ainda nao confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os convidados que ainda nao confirmaram
print("Convidados que ainda nao confirmaram")
for pessoa in nao_confirmados :
    print(pessoa)

# Enviar lembretes aos nao confirmados
print("\nEnviando lembretes para os convidados que ainda nao confirmaram.")