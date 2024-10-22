# Adicionando notas do aluno
nota_1 = float(input('Qual a primeira nota? '))
nota_2 = float(input('Qual a segunda nota? '))
nota_3 = float(input('Qual a terceira nota? '))
nota_4 = float(input('Qual a quarta nota? '))
nota_5 = float(input('Qual a quinta nota? '))


# Juntando as notas em uma string
notas = [nota_1, nota_2, nota_3, nota_4, nota_5]

# Duncao regular para calcular a media
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Funcao lambda para arredondar a media para duas casas decimais
arredondar_media = lambda media: round(media, 2)

# Calcular a media
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

# Verificar se o estudante foi aprovado
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

# Resultados
print('Notas do estudante:', notas)
print('Media das notas:', media_arredondada)
print('Situacao do estudante:', situacao)