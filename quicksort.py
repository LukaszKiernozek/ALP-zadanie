import timeit
import random
import sys
sys.setrecursionlimit(50000)

#random
A = [random.randint(0, 10000) for _ in range(10000)]

#posortowana od 0 do 9 
#A = sorted(list(range(10)) * 100)

#posortowana
#A = list(range(0, 1000))



def quicksort(A, p, r):
    if p<r :
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
        #print(f"Quicksort(A,{p},{q})")

def partition(A, p, r):
    x = A[r] #element wyznacz podzial
    i = p
    for j in range (p, r):
        if A[j]<=x:
            A[i], A[j] = A[j], A[i]
            i+=1
    A[i], A[r]=A[r], A[i]
    return i


czasy = timeit.repeat( lambda: quicksort(A.copy(), 0, len(A) - 1), repeat=5, number=10)



quicksort(A, 0, len(A) - 1)
#print(A)


print("Times:", czasy)
print("Average time:", sum(czasy) / len(czasy) / 100, "seconds per run")