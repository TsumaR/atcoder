N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for w in range(W + 1):
        # itemの重さよりdpテーブルの小さいところには入れることができないので
        if w < items[i][1]:
            dp[i + 1][w] = dp[i][w]
        else:
            # 選択するかしないかを選ぶ
            dp[i + 1][w] = max(dp[i][w], dp[i][w - items[i][1]] + items[i][0])

print(dp)
