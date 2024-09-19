# Em um cinema tem 3 filmes por semana, cada filme tem uma faixa etaria.
# O primeiro e para menores de 12 anos.
# O segundo e para maiores ou iguais a 12 anos e menores que 188 anos.
# Por fim, o terceiro filme e para maiores ou iguais a 18 anos.
# Ponto extra, saber a disponibilidade de ingressos





# Solicita a idade do cliente
idade = int(input("Por favor, digite sua idade:"))

# Verifica a idade para sugestao de filmes
if idade < 12:
    print("recomendamos o filme infantil Rei Leao.")
elif 12 <= idade < 18:
    print("Recomendadmos o filme adolescente Crepusculo")
else:
    print("Recomendamos o emocionante filme Coracao de ferro")


# Verifica a disponibilidade dos ingressos
quantidade_ingressos = 15 
if quantidade_ingressos > 0:
    print(f"{quantidade_ingressos} Ingressos estao disponiveis. Divirta-se no cinema!")
else:
    print("Desculpe, todos os ingressos estao esgotados para hoje.")