
import timeit
import random
import sys

sys.setrecursionlimit(50000)

#random
#A = [random.randint(0, 1000) for _ in range(1000)]

# Reverse sorted
#A = list(range(999, -1, -1))

#prawie posortowane
#A = list(range(900)) + [random.randint(0, 1000) for _ in range(100)]

#wiele powtorzen
A = [random.randint(0, 9) for _ in range(10000)]


def heapify(arr, n, i):

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


czasy = timeit.repeat(
    lambda: heapSort(A.copy()),
    repeat=5,
    number=10
)

heapSort(A)
#print(A)

print("Times:", czasy)
print("Average time:", sum(czasy) / len(czasy) / 10, "seconds per run")
