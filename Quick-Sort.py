import random
import numpy
numeros_aleatorios = [random.randint(1,50) for i in range(20)]
print("La lista desordenada: ",numeros_aleatorios)
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        numeros_menores = [num for num in nums[1:] if num <= pivot]
        numeros_mañores = [num for num in nums[1:] if num > pivot]
        return quick_sort(numeros_menores) + [pivot] + quick_sort(numeros_mañores)

ordenados = quick_sort(numeros_aleatorios)
print("La lista ordenada: ",ordenados)