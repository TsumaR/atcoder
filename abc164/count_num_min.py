"""
n個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と
正の整数 Aが与えられる。これらの整数から何個かの整数を選んで総和が
Aにする方法をすべて考えた時、選ぶ整数の個数の最小値を求めよ。Aにすることができない場合は -1 と出力せよ。

【制約】
・1≤n≤1001≤n≤100
・1≤a[i]≤10001≤a[i]≤1000
・1≤A≤100001≤A≤10000

5
7 3 5 1 8
12
"""

n = int(input())
a = list(map(int, input().split(' ')))
A = int(input())

dp = [[float("inf")]*(A+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
  for j in range(A+1):
    if j >= a[i]:
      dp[i+1][j] = min(dp[i][j-a[i]]+ 1, dp[i][j])
    else:
      dp[i+1][j] = dp[i][j]

print(dp[n][A])