import sys
sys.setrecursionlimit(10**7) 
h,w = map(int, input().split())
c = [list(input()) for i in range(h)]

def deep_search(x,y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#":
        return
    if c[x][y] == "g": # ゴールを見つけたら”Yes”を出力して終了
        print("Yes")
        sys.exit()
    c[x][y] == "#"
    deep_search(x+1, y)
    deep_search(x-1, y)
    deep_search(x, y+1)
    deep_search(x, y-1)

# スタート地点から開始
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j

deep_search(sx, sy)
print("No")
