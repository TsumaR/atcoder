"""
マスターオブ整数
"""

from collections import Counter
N, P = map(int, input().split())

# Pを素因数分解する
if N == 1:
    print(P)
    exit()

prime_list = []

for i in range(2, int(P**0.5) + 1):
    if P % i == 0:
        while P % i == 0:
            prime_list.append(i)
            P //= i
prime_count = Counter(prime_list)
ans = 1
for k,v in prime_count.items():
    if v >= N:
        ans *= k ** (v//N) 
print(ans)