######################              Método de ordenamiento InsertionSort        ########################################################
#Consiste en tomar uno por uno los elementos de un 
#arreglo y recorrerlo hacia su posición con respecto a los anteriormente ordenados.
#El elemento se inserta moviendo los elementos 
#superiores una posición a la derecha y ocupando la posición vacante.

import random
numeros_aleatorios = [random.randint(1,50) for i in range(20)]
print("La lista desordenada es:", numeros_aleatorios)

for i in range(1, len(numeros_aleatorios)):
    # Guardamos el valor del elemento actual de la lista
    valor_actual = numeros_aleatorios[i]
    posicion = i
    # Mientras el elemento anterior sea mayor que el valor actual, movemos el elemento anterior a la derecha
    while posicion > 0 and numeros_aleatorios[posicion - 1] > valor_actual:
        numeros_aleatorios[posicion] = numeros_aleatorios[posicion - 1]
        posicion -= 1
    # Una vez encontrada la posición correcta, insertamos el valor actual en esa posición
    numeros_aleatorios[posicion] = valor_actual
print("La lista ordenada es:", numeros_aleatorios)