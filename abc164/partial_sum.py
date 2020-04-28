"""
動的計画法で部分話問題をとく

n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 A が与えられる。
これらの整数から何個かの整数を選んで総和が A になるようにすることが可能か判定せよ。
可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。

【制約】
・1≤n≤1001≤n≤100
・1≤a[i]≤10001≤a[i]≤1000
・1≤A≤100001≤A≤10000

3
7 5 3
10
"""
n = int(input())
a = list(map(int, input().split(' ')))
A = int(input())

# DPテーブルを作る
dp = [[0]*(A+1) for _ in range(n + 1)]
# 0個の整数の和は0なのでdp[0][0]はtrueの1
dp[0][0] = 1

for i in range(n):
  for j in range(A+1):
    if j >= a[i]:
      dp[i+1][j] = dp[i][j-a[i]] or dp[i][j]
    else:
      dp[i+1][j] = dp[i][j]

if dp[n][A] == 1:
  print("True")
else:
  print("False")