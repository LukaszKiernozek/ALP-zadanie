
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


# To heapify a subtree rooted with node i
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


# Main function to do heap sort
def heapSort(arr):
    n = len(arr)

    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)


# Benchmark
czasy = timeit.repeat(
    lambda: heapSort(A.copy()),
    repeat=5,
    number=10
)

# Sort original array
heapSort(A)

#print(A)

print("Times:", czasy)
print("Average time:", sum(czasy) / len(czasy) / 10, "seconds per run")
