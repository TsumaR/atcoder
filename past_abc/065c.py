import math
N, M = map(int, input().split())
mod = 10**9 + 7
if abs(N-M) >= 2:
    print(0)
    exit()
elif N == M:
    print(2*(math.factorial(N)**2) % mod)
else:
    print(math.factorial(N)*math.factorial(M) % mod)