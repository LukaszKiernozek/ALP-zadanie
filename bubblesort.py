
import timeit
import random
import sys

sys.setrecursionlimit(50000)

# random
A = [random.randint(0, 10000) for _ in range(10000)]

# sorted from 0 to 9
# A = sorted(list(range(10)) * 100)

# sorted
# A = list(range(0, 1000))


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Benchmark
czasy = timeit.repeat(
    lambda: bubbleSort(A.copy()),
    repeat=5,
    number=10
)

bubbleSort(A)

#print(A)

print("Times:", czasy)
print("Average time:", sum(czasy) / len(czasy) / 10, "seconds per run")
