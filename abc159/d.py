import collections

N = int(input())
A = list(map(int, input().split()))

C = collections.Counter(A)
count = 0
for i in C.values():
    count += i * (i-1) // 2

for i in A:
    n = C[i]
    if n >= 2:
        print(count - n  + 1)
    else:
        print(count)