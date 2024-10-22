# Criar um programa que calcule IMC (Índice de Massa Corpórea).

# Entendimento do Problema
# O que o programa deve fazer? 
# Ele deve pedir a altura e o peso do usuário e calcular o IMC com base nesses valores.
# Como o resultado será exibido? 
# O programa deve mostrar o valor do IMC e, de preferência, 
# uma mensagem dizendo se o usuário está abaixo, dentro ou acima do peso ideal.

#  --------------------------------------------------------------------------------------------

# Peso e altura do usuario
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

# Calculo do IMC
imc = peso / (altura ** 2)

# Resultado 
print(f"Seu IMC e: {imc:.2f}")

# Validando valores
if peso <= 0 or altura <= 0:
    print("Peso e altura devem ser maiores que zero!")
else:
    if imc < 18.5:
        print ("Voce esta abaixo do peso.")
    elif 18.5 <= imc < 24.9:
        print("Voce esta com o peso normal.")
    elif 25 <= imc <29.9:
        print("Voce esta com sobrepeso.")
    else:
        print("Voce esta com obesidade.")