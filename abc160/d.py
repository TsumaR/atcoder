import itertools

N, X, Y = map(int, input().split())

# dp = [[float('inf')] * (N+1) for _ in range(N+1)]
# # dp[Y][X] = 1
# dp[X][Y] = 1

# for i in range(1,N+1):
#     for j in range(i,N+1):
#         if i == j:
#             dp[i][j] = 0
#         elif i == X and j == Y:
#             dp[X][Y] = 1
#         elif i <= X:
#             dp[i][j] = min(dp[i][j-1] + 1, dp[i][X] + abs(Y - j) + 1)
#         else:
#             dp[i][j] = min(dp[i][j-1]+ 1, abs(i - X)+ abs(Y - j) + 1 )

# dp = list(itertools.chain.from_iterable(dp))
# for i in range(1,N):
#     print(dp.count(i))

result = [0] * N

for i in range(1, N):
    for j in range(i+1, N+1):
        dist = min(abs(j-i), abs(X-i) + 1 + abs(j-Y), abs(Y-i)+1+abs(j-X))
        result[dist] += 1

for i in range(1, N):
    print(result[i])
