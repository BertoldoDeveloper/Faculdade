# Fazendo o usuario escolher um valor
a = input("escolha um valor:")
b = input("escolha um valor:")

# Definindo uma funcao chamada "adicao"
def adicao(a, b):
    resultado = a + b
    return resultado

resultado_adicao = adicao(a, b)

# Imprimindo o resultado
print(f"A adicao de {a} + {b} e:", resultado_adicao)
