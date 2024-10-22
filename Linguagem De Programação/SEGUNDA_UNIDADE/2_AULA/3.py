#  Objetos do tipo array Numpy


# Importe a biblioteca Numpy
import numpy as np

# Crie um array Numpy de numeros inteiros
my_array = np.array([1, 2, 3, 4, 5])

# Imprima o array
print("Array original:")
print(my_array)

# Realize operacoes matematicas com o array
squared_array = my_array ** 2 #Eleva cada elemento ao quadrado
sum_of_elements = np.sum(my_array) # Calcula a soma de todos os elementos

# Imprima os resultados
print("\nArrayy ao quadrado")
print(squared_array)
print("\nSoma dos elementos")
print(sum_of_elements)

# Acesse elementos do array
element_at_index_2 = my_array[2] #Acessa o elemento no indice 2
print("\nElemento do indice 2 :", element_at_index_2)