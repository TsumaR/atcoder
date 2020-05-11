"""
典型的なしゃくとり問題
全体の部分列からK以下の部分列を除くことを考えれば良い(今回は自分の提出に近い形でやった。)
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans, r, s = 0, 0, 0

"""
しゃくとり法の実装
ループ回す際に端の値を継続するだけ
合計値から左端だけを除去する
"""

for l in range(N):
    while(r < N) and (s < K):
        s += A[r]
        r += 1
    if s >= K:
        ans += N - r + 1
    s -= A[l]

print(ans)