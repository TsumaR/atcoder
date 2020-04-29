from collections import deque

h,w,n = map(int, input().split())
maze = [list(input()) for i in range(h)]

for height in range(h):
    for width in range(w):
        if maze[height][width] == "S":
            sx, sy = height, width
            
def find_shortest():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result_distance = 0
    # スタートをリセットしながら回す。
    # 都度queを設定して最初から回す。

    for hardness in range(n+1):
        # リセットされた中での距離
        d = [[float("inf")] * w for i in range(h)]
        que = deque([])
        que.append((sx, sy))
        d[sx][sy] = 0
        # 現在のスタート値から次のレベルに到達するまでにかかる距離をbfsで検索
        while que:
            p = que.popleft()
            # リセットされた中でゴールについたら
            if maze[p[0]][p[1]] == str(hardness+1):
                result_distance += d[p[0]][p[1]]
                sx = p[0]
                sy = p[1]
                break
            for i in range(4):
                nx = p[0] + dx[i]
                ny = p[1] + dy[i]
                if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != "X" and d[nx][ny] == float("inf"):
                    que.append((nx, ny))
                    d[nx][ny] = d[p[0]][p[1]] + 1
    return result_distance
        
ans = find_shortest()
print(ans)