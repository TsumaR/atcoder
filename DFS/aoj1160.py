w, h = map(int, input().split())
sea_region = [list(map(int, input().split())) for _ in range(h)]

# まだ探索済みでない頂点 v を一つ選んで v を始点とした DFS を行う
c_w = [0, 1, 1, 1, 0, -1, -1, -1]
c_h = [1, 1, 0, -1, -1, -1, 0, 1]  

def dfs(G, x, y):
    if not(0 <= x < w) or not(0 <= y < h) or G[y][x] == 0:
        return 
    if G[y][x] == 1:
        G[y][x] = 0
        for i in range(8):
            nx = x + c_w[i]
            ny = y + c_h[i]
            dfs(G, nx, ny)

count = 0
for i in range(h):
    for j in range(w):
        if sea_region[i][j] == 1:
            count += 1
        dfs(sea_region, j, i)

print(count)