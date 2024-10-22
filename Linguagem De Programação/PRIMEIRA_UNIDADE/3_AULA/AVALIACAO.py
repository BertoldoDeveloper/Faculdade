# Vamos pensar na solução do problema apresentado no início desta aula.
# Precisamos criar um programa que seja capaz de percorrer todos os filmes
# (Filme 1, Filme 2, Filme 3, Filme 4 e Filme 5) e de atribuir a cada um
# deles uma nota de 1 a 5.
# Repare que é importante sempre disponibilizar uma forma de a pessoa encerrar
# o programa, caso queira.



# Lista de filmes

filmes = ["Rei Leao", "Covil de Ladroes", "Madagascar", "Missao Impossivel", "Jhon Wick"]

# Mensagem de Boas-vindas

print("Bem-Vindo a classificacao de filmes!")
print("Voce tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar.\n")


# Loop para iterar sobre cada filme na lista 

for filme in filmes:
    # Solicita a classificacao do usuario
    classificacao = input(f"Como voce classificaria '{filme}' de 1 a 5? (ou 0 para parar): ")

    # Verifica se o usuario deseja parar
    if classificacao == '0':
        print("Que pena que voce nao ira classificar mais os filmes.")
        break # Encerra o loop principal

    # Converte a classificacao para um numero inteiro
    classificacao = int(classificacao)

    # Verifica se a classificacao esta dentro do intervalo valido
    if classificacao < 1 or classificacao > 5:
        print("Por favor, digite uma classificacao valida de 1 a 5.")
    else:
        # Exibe a classificacao e passa para o proximo filme
        print(f"Voce classificaou '{filme}' com {classificacao} estrelas.\n")

# Mensagem de agradecimento ao finalizar
print("Obrigado por classificar os filmes!")