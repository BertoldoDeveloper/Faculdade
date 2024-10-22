# Objetivo:
# Desenvolvimento de um diagrama de blocos para o cálculo da média de dois valores.

# Inicio
def calcular_media():
    # Entrada dos valores
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    
    # Soma dos valores
    soma = valor1 + valor2
    
    # Cálculo da média
    media = soma / 2
    
    # Exibição do resultado
    print(f"A média dos valores é: {media}")

# Chamar a função para iniciar o cálculo
calcular_media()
# Fim