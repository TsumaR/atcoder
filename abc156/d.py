import math
N, A, B = map(int, input().split())
mod = 10**9 + 7 

def pow(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans
print(pow(2, N))

