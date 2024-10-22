# Listas com Python

cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa']
for cor in cores:
    print(f'Posicao = {cores.index(cor)}, cor = {cor}')






# List Comps

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print("Antes da listcomp = ", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\nDepois da listcomp = ", linguagens)




# Funcao Map

# Aplica a uma sequencia em toda a sequencia
# Map(funcao,sequencia)

precos_em_dolares = [100, 50, 75, 120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)

# Funcao filter

# Filtra elementos de uma sequencia com base em uma funcao de teste (retorna True or False)
# filter(funcao_teste, sequencia)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)


#  Tuplas
# Tuplas sao objetos imutaveis 

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais = {type(vogais)}")
for p, x in enumerate (vogais) :
    print (f"Posicao = {p}, valor = {x}")
    