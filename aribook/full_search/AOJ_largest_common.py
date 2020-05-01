N = int(input())

X = []
Y = []

for i in range(N):
    X.append([i for i in input()])
    Y.append([i for i in input()])

def find_longest_common(x,y):
    dp = [[0] * (len(x)+1) for _ in range(len(y) + 1)]
    for i in range(len(y)):
        for j in range(len(x)):
            if x[j] == y[i]:
                # dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j], dp[i][j+1])
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    print(dp[len(y)][len(x)])
            
for s in range(N):
    find_longest_common(X[s], Y[s])
