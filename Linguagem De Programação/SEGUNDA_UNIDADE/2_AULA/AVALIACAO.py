# Como podemos usar conjuntos (sets) para identificar as diferentes regiões dos participantes 
# do evento científico, dicionários para categorizar suas afiliações e arrays NumPy para analisar 
# as áreas de interesse?


# Importe as bibliotecas necessarias
import numpy as np

# Dados dos participantes
participantes = [
    {
        "nome":"Alice",
        "localizacao":"EUA",
        "afiliacao":"Universidade A",
        "interesses":["Fisica","Astronomia"]
    },

    {
        "nome":"Bob",
        "localizacao":"Brasil",
        "afiliacao":"Instituto B",
        "interesses":["Biologia","Astronomia"]
    },

    {
        "nome":"Charlie",
        "localizacao":"India",
        "afiliacao":"Instituto C",
        "interesses":["Quimica", "Engenharia"]
    }
]

# Usando sets para identificar diferentes regioes dos participantes
regioes = set(participante["localizacao"] for participante in participantes)

# Usando o dicionario para categorizar afiliacoes
afiliacoes = {}
for participante in participantes:
    afiliacao = participante["afiliacao"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

# Usando Numpy para analisar areas de interesse 
areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante["interesses"]])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

# Resultados
print("Regioes dos participantes:", regioes)
print("Afiliacoes dos participantes:")
for afiliacao, nomes in afiliacoes.items():
    print(f"{afiliacao}:{','.join(nomes)}")
print("Area de interesse mais popular:", area_mais_popular)
