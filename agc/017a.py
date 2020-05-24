from math import factorial
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))
N, P = map(int, input().split())
A = list(map(int, input().split()))

modA = [i % 2 for i in A]
odd = modA.count(1)
even = modA.count(0)

even_count = 1
for i in range(1, even+1):
    even_count += combinations_count(even, i)

if P == 0:
    """
    evenからは好きなだけ選べる
    それに対してoddから偶数個を選ぶ
    """
    odd_count = 0
    for i in range(0,odd+1,2):
        odd_count += combinations_count(odd, i)
    print(even_count * odd_count)
else:
    """
    evenから好きなだけ選べる
    oddから奇数個を選ぶ
    """
    odd_count = 0
    for i in range(1,odd+1,2):
        odd_count += combinations_count(odd, i)
    print(even_count * odd_count)

