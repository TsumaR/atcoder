import itertools

N, K = map(int ,input().split())

d = []
A = []

for i in range(K):
    d.append(int(input()))
    a = list(map(int, input().split()))
    A.append(a)

ans = 0
A = itertools.chain.from_iterable(A)
A = set(A)
for i in range(1,N+1):
    if i not in A:
        ans += 1

print(ans)