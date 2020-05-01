N = int(input())
ashiba = list(map(int, input().split()))

# dp配列の準備
dp = ["inf"] * N

dp[0] = 0
dp[1] = abs(ashiba[1] - ashiba[0])
for i in range(2, N):
    dp[i] = min(dp[i-2] + abs(ashiba[i] - ashiba[i-2]), dp[i-1] + abs(ashiba[i] - ashiba[i-1]))

print(dp[N-1])