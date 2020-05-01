N = int(input())
A = list(map(int, input().split()))

max_num = sum(A)
dp = [False] * (max_num+1)
dp[0] = True

for i in range(N):
    for j in reversed(range(max_num + 1)):
        if j - A[i] >= 0 and dp[j-A[i]]:
            dp[j] = True
print(sum(dp))
# dp = [[0] * (max_num) for _ in range(N + 1)]
# dp[0][0] = 1

# for i in range(N):
#     for j in range(max_num):
#         if j < A[i]:
#             dp[i+1][j] = dp[i][j]
#         else:
#             dp[i+1][j] = max(dp[i][j-A[i]]+1, dp[i][j])
# print(dp[])