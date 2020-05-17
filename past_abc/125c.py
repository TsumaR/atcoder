"""
GCD on Blackboard
"""
import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

N = int(input())
A = list(map(int, input().split()))


print(max(G))