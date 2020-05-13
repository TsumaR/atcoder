from collections import Counter

S = list(input())
C = Counter(S)
if len(S) == 1:
    print('YES')
    exit()
"""
条件を考えてみる
一種類の字しかない時は回文
２種類の時も，長さが２より大きい時は回文
同じ文字をに連続で並べないといけない時に回文になる。

ある文字が他の文字よりも2つ以上多い時には回文になる。
"""

L = C.values()
if len(L) <= 1:
    print('NO')
elif len(L) == 2 and len(S) > 2:
    print('NO')
elif max(L) - min(L) >= 2:
    print('NO')
else:
    print('YES')