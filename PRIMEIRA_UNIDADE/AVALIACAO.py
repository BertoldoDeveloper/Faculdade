# Como você pode aplicar seus conhecimentos em programação 
# em Python para criar uma calculadora de desconto?
# Que estruturas condicionais em Python você pode usar para 
# verificar se o desconto está dentro de limites aceitáveis?




# Solicita ao usuario que insira o valor do produto e o percentual de desconto 
valor_produto = float(input('Digite o valor do produto: R$ '))
percentual_desconto = float(input('Digite o percentual de desconto: '))

# Verifica se o percentual de desconto esta dentro dos limites aceitaveis (0 - 100%)
if percentual_desconto < 5 or percentual_desconto > 20:
    print('Erro: O percentual de desconto deve estar entro 5% e 20%')
else:
    # Calcula o valor do desconto
    desconto = valor_produto * (percentual_desconto / 100)

    # Calcula o valor final da compra
    valor_final = valor_produto - desconto

    # Exibe o valor final da compra
    print(f"Valor com desconto: R$ {valor_final:.2f}")

    