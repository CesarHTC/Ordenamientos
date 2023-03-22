######################              Método de ordenamiento Bubble-Sort        ########################################################
#El ordenamiento de intercambio (también conocido como bubble sort) es un algoritmo de ordenamiento que funciona comparando
#pares adyacentes de elementos en una lista y intercambiándolos si están en el orden equivocado. El algoritmo sigue haciendo 
#esto hasta que toda la lista esté ordenada

#El algoritmo de intercambio funciona de la siguiente manera:

#1-Comenzando desde el primer elemento de la lista, compara el elemento actual con el siguiente elemento en la lista.
#2-Si el elemento actual es mayor que el siguiente elemento, intercambia los dos elementos.
#3-Continúa comparando y haciendo intercambios hasta que llegues al final de la lista.
#4-En este punto, el elemento más grande debería estar en la última posición de la lista.
#5-Repite los pasos 1 a 4, pero esta vez, comienza desde el primer elemento hasta el penúltimo elemento de la lista.
#5-Continúa repitiendo este proceso para cada elemento de la lista, hasta que toda la lista esté ordenada.

import random
numeros_aleatorios = [random.randint(1,10) for i in range(5)]
print("La lista desordenada es:", numeros_aleatorios)
#-Comenzando desde el primer elemento de la lista
for j in range(len(numeros_aleatorios)):
    valor = numeros_aleatorios[j]
    posicion = j
    #compara el elemento actual con el siguiente elemento en la lista hasta llegar al final de la lista
    for i in range(j+1, len(numeros_aleatorios)): 
        if numeros_aleatorios[i] < valor:
            temp = numeros_aleatorios[i]
            numeros_aleatorios[i] = numeros_aleatorios[j]
            numeros_aleatorios[j] = temp
    #Si el elemento actual es mayor que el siguiente elemento, intercambia los dos elementos        
   
print("Lista ordenada:", numeros_aleatorios)

