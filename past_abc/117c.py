
"""
全探索は無理なオーダー
N個のこま，
M - N回の移動が必要
−＞間の距離の長いのを移動しないように配置すれば良い
"""
N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()
if N >= M:
    print(0)
    exit()

dist = [X[i+1] - X[i] for i in range(M-1)]
dist.sort(reverse=True)

count = sum(dist)
for i in range(N-1):
    count -= dist[i]

print(count)