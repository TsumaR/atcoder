"""
二文字をショートカット
長さは1000以下
ショートカットの組み合わせは合計で16通り
全てに対して試して，登場回数の多い二つをとる（二つをとっていけるかは微妙，全探索する必要があるかもしれない）
やはり全探索だった。
dp = [0] * Nのdp
Xを適用し，それぞれに対し，何文字目までいくつかの文字で表せたかをDPで計算する
"""
import itertools

N = int(input())
C = list(input())
C = ['X'] + C
button = ['A', 'B', 'X', 'Y']
shortcut = []
# ショートカット候補をリストアップ
for i in button:
    for j in button:
        shortcut.append([i, j])

comb = list(itertools.combinations(shortcut, 2))

inf = float("INF")

ans = inf
for L,R in comb:
    dp = [i for i in range(N+1)]
    for i in range(1,N):
        if L[0] == C[i] and L[1] == C[i+1]:
            dp[i+1] = min(dp[i+1], dp[i-1] + 1)
            dp[i] = min(dp[i], dp[i-1] + 1)
        else:
            dp[i+1] = min(dp[i+1], dp[i] + 1)
    for j in range(1,N):
        if R[0] == C[j] and R[1] == C[j+1]:
            dp[j+1] = min(dp[j+1], dp[j-1] + 1)
            dp[j] = min(dp[j], dp[j-1] + 1)
        else:
            dp[j+1] = min(dp[j+1], dp[j] + 1)
    print(L, R)
    print(dp)
    ans = min(ans, dp[N-1])

print(ans)