"""
easy linear programmingの問題(LP，ELP)
線形計画問題
にちかい
"""

A, B, C, K = map(int, input().split())

a = K - A
b = a - B
c = 0
if b > 0:
    c = K - b

if a <= 0:
    print(K)
elif b > 0:
    print(A - b)
else:
    print(A)
