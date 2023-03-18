#La selección de ordenamiento (Selection Sort) es un algoritmo de ordenamiento simple que funciona 
#bien para listas pequeñas y para listas en las que los elementos ya están en su mayoría ordenados.
"""
El algoritmo de selección de ordenamiento funciona de la siguiente manera:

1-Encuentra el elemento más pequeño en la lista.
2-Intercambia ese elemento con el primer elemento de la lista.
3-Ahora, considera el resto de la lista (sin el primer elemento) y encuentra el elemento más pequeño en esa lista.
4-Intercambia ese elemento con el segundo elemento de la lista.
5-Continúa este proceso hasta que toda la lista esté ordenada.
"""
import random
import numpy
numeros_aleatorios = [random.randint(1,50) for i in range(20)]
print("La lista desordenada es:", numeros_aleatorios)

for i in range(len(numeros_aleatorios)):
    # Encuentra el elemento más pequeño en la lista no ordenada
    min_index = i
    for j in range(i+1, len(numeros_aleatorios)):
        if numeros_aleatorios[j] < numeros_aleatorios[min_index]:
            min_index = j
    
    # Intercambia el elemento más pequeño con el primer elemento no ordenado
    temp = numeros_aleatorios[i]
    numeros_aleatorios[i] = numeros_aleatorios[min_index]
    numeros_aleatorios[min_index] = temp


        




print("La lista ordenada es:", numeros_aleatorios)
