# Ordenações
from time import time
import numpy as np
from math import floor

# Making a heap
class heap:
    def __init__(self):
        self.vector = []
        
    def build(vector):
        pass

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

# Ordenação por SelectionSort
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

# Ordenação por InsertionSort
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

# Ordenação por MergeSort
def mergeSort(vector, aux, i, f):
    if i < f:
        m = floor((i + f) / 2)
        mergeSort(vector, aux, i, m)
        mergeSort(vector, aux, m + 1, f)
        merge(vector, aux, i, m, f)
    return vector

def merge(vector, aux, i, m, f):
    i1 = i
    i2 = i
    i3 = m + 1
    while i2 <= m and i3 <= f:
        if vector[i2] < vector[i3]:
            aux[i1] = vector[i2]
            i1 += 1
            i2 += 1
        else:
            aux[i1] = vector[i3]
            i1 += 1
            i3 += 1
    while i2 <= m:
        aux[i1] = vector[i2]
        i1 += 1
        i2 += 1
    while i3 <= f:
        aux[i1] = vector[i3]
        i1 += 1
        i3 += 1
    for j in range(i, f+1):
        vector[j] = aux[j]

# Ordenação por RadixSort
def radixSort(vector, base, d):
    n = len(vector)
    queue = []
    for i in range(base):
        queue.append([])
    i = 0
    factor = 1
    while i < d:
        for j in range(n):
            queue[floor(vector[j] / factor) % base].append(vector[j])
        
        j = 0
        k = 0
        while j < base:
            while len(queue[j]) != 0:
                vector[k] = queue[j].pop(0)
                k += 1
            j += 1
        
        factor *= base
        i += 1
    return vector

# Função principal
def main():
    vector = np.random.randint(999, size = 1000)
    
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
    
    st = time()
    v = vector.copy()
    mergeSort(v, v, 0, len(v)-1)
    et = time()
    print('Merge Sort: ', et - st)
    
    st = time()
    v = vector.copy()
    v1 = radixSort(v, 10, 3)
    et = time()
    print('Radix Sort: ', et - st)
    
main()
