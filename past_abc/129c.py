N, M = map(int, input().split())
A = set([int(input()) for _ in range(M)])

"""
DPを考える
"""

result = [0] * (N+1)
result[0] = 1
if 1 not in A:
    result[1] = 1
mod = 10**9 + 7
for i in range(2,N+1):
    if i not in A:
        result[i] = (result[i-1] + result[i-2])

print(result[N]%mod)