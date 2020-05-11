N = int(input())
T = [int(input()) for _ in range(N)]

"""
1 <= N <= 4という制約
"""

ans = float("INF")
# 高橋くん側で焼くを1としてbitで表す
# 焼くのにかかる合計
total = sum(T)

for i in range(0, 1 << N):
    takahashi = 0
    for j in range(N):
        if (i >> j) & 1:
            takahashi += T[j]
    fin_time = max(takahashi, total - takahashi)
    ans = min(ans, fin_time)

print(ans)