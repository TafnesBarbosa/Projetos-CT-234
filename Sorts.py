# Ordenações
from time import time
import numpy as np
from math import floor

# Making a heap
class heap:
    def __init__(self, tipo):
        self.vector = []
        self.tipo = tipo
        
    def __str__(self):
        return str(self.vector)
        
    def sift(self, i, n):
        esq = 2 * i
        dire = 2 * i + 1
        maimenor = i
        if self.tipo == 'max':
            if esq <= n and self.vector[esq - 1] > self.vector[i - 1]:
                maimenor = esq
            if dire <= n and self.vector[dire - 1] > self.vector[maimenor - 1]:
                maimenor = dire
            if maimenor != i:
                aux = self.vector[i - 1]
                self.vector[i - 1] = self.vector[maimenor - 1]
                self.vector[maimenor - 1] = aux
                self.sift(maimenor, n)
        elif self.tipo == 'min':
            if esq <= n and self.vector[esq - 1] < self.vector[i - 1]:
                maimenor = esq
            if dire <= n and self.vector[dire - 1] < self.vector[maimenor - 1]:
                maimenor = dire
            if maimenor != i:
                aux = self.vector[i - 1]
                self.vector[i - 1] = self.vector[maimenor - 1]
                self.vector[maimenor - 1] = aux
                self.sift(maimenor, n)
    
    def build(self, vector):
        self.vector = vector
        self.n = len(vector)
        n = self.n
        for i in range(floor(n / 2), 0, -1):
            self.sift(i, n)

    def Max(self):
        if self.tipo == 'max':
            return self.vector[0]
        else:
            return 'Error, minimum heap.'
    
    def Min(self):
        if self.tipo == 'min':
            return self.vector[0]
        else:
            return 'Error, maximum heap.'
    
    def ExtractMax(self):
        if self.tipo == 'max':
            if self.n < 1:
                return 'heap underflow'
            else:
                Max = self.vector[0]
                self.vector[0] = self.vector[-1]
                self.vector.pop()
                self.n -= 1
                self.sift(1, self.n)
                return Max
        else:
            return 'Error, minimum heap.'
            
    def ExtractMin(self):
        if self.tipo == 'min':
            if self.n < 1:
                return 'heap underflow'
            else:
                Min = self.vector[0]
                self.vector[0] = self.vector[-1]
                self.vector.pop()
                self.n -= 1
                self.sift(1, self.n)
                return Min
        else:
            return 'Error, minimum heap.'
    
    def Modify(self, k, x):
        if self.tipo == 'max':
            if k > self.n or k < 1:
                return 'index error'
            else:
                self.vector[k - 1] = x
                while k > 1 and self.vector[floor(k / 2) - 1] < self.vector[k - 1]:
                    aux = self.vector[k-1]
                    self.vector[k-1] = self.vector[floor(k / 2) - 1]
                    self.vector[floor(k / 2) - 1] = aux
                    k = floor(k / 2)
                self.sift(k, self.n)
        else:
            if k > self.n or k < 1:
                return 'index error'
            else:
                self.vector[k - 1] = x
                while k > 1 and self.vector[floor(k / 2) - 1] > self.vector[k - 1]:
                    aux = self.vector[k-1]
                    self.vector[k-1] = self.vector[floor(k / 2) - 1]
                    self.vector[floor(k / 2) - 1] = aux
                    k = floor(k / 2)
                self.sift(k, self.n)
    
    def Insert(self, x):
        self.vector.append(0)
        self.n += 1
        self.Modify(self.n, x)
    
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

# Ordenação por HeapSort
def heapSort(vector):
    h = heap('max')
    h.build(vector)
    for i in range(h.n, 0, -1):
        aux = h.vector[i - 1]
        h.vector[i - 1] = h.vector[0]
        h.vector[0] = aux
        h.sift(1, i - 1)
    return h.vector

# Ordenção por QuickSort
def quickSort(vector, mini, maxi):
    if mini < maxi:
        p = Partition(vector, mini, maxi)
        quickSort(vector, mini, p - 1)
        quickSort(vector, p + 1, maxi)

def Partition(vector, left, right):
    pivot = vector[left - 1]
    l = left + 1
    r = right
    while True:
        while l < right and vector[l - 1] < pivot:
            l += 1
        while r > left and vector[r - 1] >= pivot:
            r -= 1
        if l >= r:
            break
        aux = vector[l - 1]
        vector[l - 1] = vector[r - 1]
        vector[r - 1] = aux
    vector[left - 1] = vector[r - 1]
    vector[r - 1] = pivot
    return r

# Função principal
def main():
    vector = np.random.randint(999, size = 10)
    
    print(vector)
    
    st = time()
    v1 = bubbleSort(vector.copy())
    et = time()
    print('Bubble Sort: ', et - st)
    print(v1)
    
    st = time()
    v1 = selectionSort(vector.copy())
    et = time()
    print('Selection Sort: ', et - st)
    print(v1)
    
    st = time()
    v1 = insertionSort(vector.copy())
    et = time()
    print('Insertion Sort: ', et - st)
    print(v1)
    
    st = time()
    v = vector.copy()
    v1 = mergeSort(v, v, 0, len(v)-1)
    et = time()
    print('Merge Sort: ', et - st)
    print(v1)
    
    st = time()
    v = vector.copy()
    v1 = radixSort(v, 10, 3)
    et = time()
    print('Radix Sort: ', et - st)
    print(v1)
    
    st = time()
    v = vector.copy()
    v1 = heapSort(v)
    et = time()
    print('Heap Sort: ', et - st)
    print(v1)
    
    st = time()
    v = vector.copy()
    v1 = quickSort(v, 1, len(v))
    et = time()
    print('Quick Sort: ', et - st)
    print(v1)
    
    st = time()
    v = vector.copy().tolist()
    v.sort()
    et = time()
    print('Sort: ', et - st)
    print(v1)
    
main()
