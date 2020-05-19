"""
素直に実装するとN**9
"""

import itertools

N = int(input())
L = list(map(int, input().split()))


count = 0
for a in L:
    l = L[a:]
    comb = list(itertools.combinations(L, 2))
    for b,c in comb:
        if abs(b-c) < a < b+c:
            count += 1
print(count)
