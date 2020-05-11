"""
ぱっと見深さ優先探索で解ける
通った道を#にする

ダメだった。
全部の候補の中から最善を選ぶ場合BFS(幅優先探索を用いる)
最短で動く必要があるので，各始点から他の点全てに対して，最短経路を探索して一番長いのをansとして残す
"""
import sys
import copy
from collections import deque

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]

dw = [1, 0, -1, 0]
dh = [0, -1, 0, 1]

ans = 0
for sh in range(H):
    for sw in range(W):
        # 壁スタートはダメ
        if S[sh][sw] == "#":
            continue
        # BFSのための準備
        d = [[float("inf")] * W for i in range(H)]
        d[sh][sw] = 0
        que = deque((sh, sw))

        while que:
            print(que)
            h, w = que.popleft()
            for i in range(4):
                nh = h + dh[i]
                nw = w + dw[i]
                if not(0 <= nh < H) or not(0 <= nw < W) or S[nh][nw] == "#" or d[nh][nw] != float("inf"):
                    continue
                else:
                    d[nh][nw] = d[h][w] + 1
                    que.append((nh, nw))
        print(d)
        ans = max(ans, max([max(dist) for dist in d]))

        


print(ans)