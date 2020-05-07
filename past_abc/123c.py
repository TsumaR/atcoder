import math

N = int(input())
numbers = list(int(input()) for _ in range(5))

M = min(numbers)

A = 5 + math.ceil(N / M) -1
print(A)