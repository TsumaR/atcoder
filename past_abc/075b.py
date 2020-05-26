import copy
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
S_result = [[0]*(W+2) for _ in range(H+2)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            for x,y in zip(dx,dy):
                if S_result[i+y+1][j+x+1] != "#":
                    S_result[i+y+1][j+x+1] += 1
            S_result[i+1][j+1] = "#"
            
for h in S_result[1:H+1]:
    print("".join(map(str, h[1:W+1])))