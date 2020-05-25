from collections import Counter

N = int(input())
S = list(input())

C = Counter(S)
count = 1
mod = 10**9 + 7
for i in C.values():
    count *= i+1
print((count-1)%mod)