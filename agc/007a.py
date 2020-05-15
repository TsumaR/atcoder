"""
深さ優先探索
goalにつけるかを判定する
通った点は.に書き換える。
"""
from itertools import chain
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

def dfs(x,y):
    if not(0 <= x <= W-1) or not(0 <= y <= H-1) or A[y][x] == ".":
        return
    if x == W-1 and y == H-1:
        A[y][x] = "."
        if "#" not in chain.from_iterable(A):
            print("Possible")
            exit()
    A[y][x] = "."
    dfs(x+1, y)
    dfs(x, y+1)

dfs(0,0)
print("Impossible")
