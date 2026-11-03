
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


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

czasy = timeit.repeat(
    lambda: bubbleSort(A.copy()),
    repeat=5,
    number=10
)

bubbleSort(A)
#print(A)

print("Times:", czasy)
print("Average time:", sum(czasy) / len(czasy) / 10, "seconds per run")
