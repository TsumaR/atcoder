import fractions
from functools import reduce

N = int(input())
T = [int(input()) for _ in range(N)]

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(L):
    return reduce(lcm_base, L, 1)

print(lcm(T))