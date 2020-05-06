# 選ぶ数で場合わけすれば良い

N, K = map(int, input().split())
A = list(range(N+1))
M = 10 ** 9 + 7

mini = sum(A[0:K])
most = sum(A[-K:])
# first_count = most -mini + 1
count = most - mini + 1

for i in range(K, N+1):
    most +=  A[-(i+1)]
    mini += A[i]
    count += (most- mini + 1)

print(count % M)