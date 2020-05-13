"""
オイラー間数値の問題
1,2,…,N1,2,…,N  のうち、NN と互いに素であるものの個数を求めよ。

答え
素因数分解したときに現れる素数をp1，p2，p3...とした時
N(1 ー 1/p1)(1 - 1/p2)(1 - 1/p3)
2の倍数を除去，3の倍数を除去，といった感じ
O(√N)
"""
import copy


p = N = int(input())
prime_numbers = []
d = 2
ans = 1 * N

while d*d <= p:
    if N % d == 0:
        ans *= 1 - 1/d
        while N % d == 0: N //= d
    d += 1

if N > 1:
    ans *= 1 - 1/N

print(int(ans))
