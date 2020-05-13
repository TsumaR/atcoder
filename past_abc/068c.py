 """
 setで論理計算する
 この解放の場合，両方のリストに含まれているというのをfor回して探索するとTLE
 setで集合演算すると通る
 積集合
"""

N, M = map(int, input().split())
starts = []
goals = []
for _ in range(M):
    s, g = map(int, input().split())
    if s == 1:
        starts.append(g)
    elif g == N:
        goals.append(s)

ans = set(starts) & set(goals)

if len(ans) >= 1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")