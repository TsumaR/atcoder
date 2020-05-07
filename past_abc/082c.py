from collections import Counter

N = int(input())
A = list(map(int, input().split()))

C = Counter(A)
count = 0
for k, v in C.items():
    if k > v:
        count += v
    else:
        count += v - k

print(count)