from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

"""
グラフの最短経路問題
１からたどる
最短経路の時，たどる前にいた点を答えとして収納すれば良い
"""
ans = [0] * (N + 1)
neighbor = [[] for _ in range(N+1)]

for a,b in AB:
    neighbor[a].append(b)
    neighbor[b].append(a)

que = deque([1])
while len(que) > 0:
    s = que.popleft()
    
    for i in neighbor[s]:
        if ans[i] == 0:
            ans[i] = s
            que.append(i)

if 0 not in ans[2:]:
    print("Yes")
else:
    print("No")
    exit()

for i in ans[2:]:
    print(i)