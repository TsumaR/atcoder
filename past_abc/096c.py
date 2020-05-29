H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

DX = [-1,0,1,0]
DY = [0,1,0,-1]
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            count = 0
            for dx,dy in zip(DX, DY):
                if H-1>=h-dy >= 0 and W-1>=w-dx >= 0 and S[h-dy][w-dx] == ".":
                    count += 1
            if count == 4:
                print("No")
                exit()
print("Yes")ke