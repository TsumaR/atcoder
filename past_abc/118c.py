import fractions
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

print(gcd_list(A))