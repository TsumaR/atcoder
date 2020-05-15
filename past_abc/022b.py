from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N))]

C = Counter(A)

ans = 0
for k,v in C.items():
    if v >= 2:
        ans += v - 1

print(ans)