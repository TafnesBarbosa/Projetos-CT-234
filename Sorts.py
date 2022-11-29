# Ordenações
from time import time
import numpy as np

# Ordenação por BubbleSort
def bubbleSort(vector):
    n = len(vector)
    for j in range(n):
        for i in range(1, n-j):
            if vector[i-1] >= vector[i]:
                aux = vector[i]
                vector[i] = vector[i-1]
                vector[i-1] = aux
    return vector
    
def selectionSort(vector):
    n = len(vector)
    for j in range(n-1):
        aux_min = j
        for i in range(j+1, n):
            if vector[i] < vector[aux_min]:
                aux_min = i
        aux = vector[aux_min]
        vector[aux_min] = vector[j]
        vector[j] = aux
    return vector
    
def insertionSort(vector):
    n = len(vector)
    for i in range(1, n):
        aux = vector[i]
        for j in range(i, -1, -1):
            if aux < vector[j-1]:
                vector[j] = vector[j-1]
            else:
                break
        vector[j] = aux
    return vector
    
def main():
    vector = np.random.randint(1000, size = 1000)
    st = time()
    bubbleSort(vector.copy())
    et = time()
    print('Bubble Sort: ', et - st)
    st = time()
    selectionSort(vector.copy())
    et = time()
    print('Selection Sort: ', et - st)
    st = time()
    insertionSort(vector.copy())
    et = time()
    print('Insertion Sort: ', et - st)
    
main()
