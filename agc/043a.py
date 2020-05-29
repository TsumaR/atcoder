H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

count = [[100000] * W for _ in range(W)]
count[0][0] = 0 if S[0][0] == "." else 1


for i in range(H):
    for j in range(W):
        if i + j == 0:
            continue
        X, Y = 10**6, 10**6
        if i > 0:
            if S[i][j] == "#" and S[i-1][j] == ".":
                X = count[i-1][j] + 1
            else:
                X = count[i-1][j]
        if j > 0:
            if S[i][j] == "#" and S[i][j-1] == ".":
                Y = count[i][j-1] + 1
            else:
                Y = count[i][j-1]
        count[i][j] = min(X, Y)

print(count[H-1][W-1])