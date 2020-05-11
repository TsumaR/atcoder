"""
縦横300以下なので全探索できそう
まず横を切ることを考える
次に縦を切る

考え方としては正しかったっぽい
けど，他の人に比べて遅い
再帰を用いる考え方もあったらしい
"""

import numpy as np

H, W, K = map(int, input().split())

A = np.array([list(input()) for _ in range(H)])
ans = np.array([[0] * W for _ in range(H)])

k = 0
n = 1
c = 0

# まず横に切る
for i in range(H):
    if "#" not in A[i]:
        ans[i] = ans[i-1]
    else:
        NP = A[k:i+1,]
        for j in range(W):        
            if "#" not in NP[:,j]:
                ans[k:i+1,j] = n
            else:
                c += 1
                if c >= 2:
                    n += 1
                    c = 1
                ans[k:i+1,j] = n
        c = 0
        n += 1
        k = i + 1

# if "#" not in A[H-1]:
#     ans[H-1] = ans[H-2]

for i in ans:
    print(*i, sep=" ")