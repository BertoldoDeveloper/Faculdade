# Definindo uma funcao chamada "e_par"
def e_par(numero) :
    # Operador modulo %
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = 11
if e_par(numero) :
    print(f"{numero} e um numero par.")
else:
    print(f"{numero} e um numero impar.")
