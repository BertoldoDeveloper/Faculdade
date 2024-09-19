# Automatize a media de nota dos alunos com Phyton


# Preciso saber a nota das 4 unidades
# Ultilizamos a funcao int(), pois sem ela o Phyton entenderia que as notas seriam uma String

Nota_1 = int(input("Digite a primeira nota:"))
Nota_2 = int(input("Digite a segunda nota:"))
Nota_3 = int(input("Digite a terceira nota:"))
Nota_4 = int(input("Digite a quarta nota:"))


# Agora preciso de uma condicao para a aprovacao do aluno

media = (Nota_1+Nota_2+Nota_3+Nota_4)/4

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Agora prceiso mostrar a media final e a situacao do aluno

print(f"A media das notas e: {media}")
print(f"Situacao do aluno: {situacao}")