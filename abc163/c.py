import collections

N = int(input())
A = list(map(int, input().split()))

C = collections.Counter(A)

for i in range(1, N+1):
    print(C[i])
