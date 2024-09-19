# add(), in e remove()

# Criando um conjundo vazio 
meu_conjunto = set()

# Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

# Imprimindo o conjunto
print("Conjunto apos adicionar elementos:", meu_conjunto)

# Verificando se um elemento esta no conjunto
elemento = 20
if elemento in meu_conjunto :
    print(f"{elemento} esta no conjunto.")
else:
    print(f"{elemento} nao esta no conjunto")

# Removendo um elemento do conjunto
meu_conjunto.remove(20)

# Imprimindo o conjunto altualizado
print(f"Conjunto apos remover o elemento 20", meu_conjunto)