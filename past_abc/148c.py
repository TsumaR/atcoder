"""
最小公倍数を求めることできる
"""

import fractions

A, B = map(int, input().split())
def lcm(a, b):
    g = fractions.gcd(a, b)
    L = a * b // g
    return L

print(lcm(A, B))