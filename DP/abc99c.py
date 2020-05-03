N = int(input())

dp = [0] * (N+1)

dp[0] = 0

pow6 = [6**i for i in range(int(N**(1/6))+2)]
pow9 = [9**i for i in range(int(N**(1/9))+2)]


for n in range(1,N+1):
    dp[n] = n
    for i in pow6[1:]:
        if n > i:
            dp[n] = min(dp[n], dp[n - i] + 1)
    for j in pow9[1:]:
        if n > j:
            dp[n] = min(dp[n], dp[n - j] + 1)

print(dp[N])
