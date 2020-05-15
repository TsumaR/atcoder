import numpy as np

N = int(input())
A = list(map(int, input().split()))

x = np.argsort(A)[::-1]
for i in x:
    print(i + 1)