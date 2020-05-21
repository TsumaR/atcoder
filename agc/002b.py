N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

"""
ボールの数が入ったリストと，赤い玉が一回でもきたことがあるかのリスト
どちらもが０じゃないのが，終わったときに赤が入っている可能性のあるリスト
ただし，ボールリストが０になる時，seenは０になる
"""
ball_list = [1] * (N+1)
seen = [0] * (N+1)
ball_list[0] = 0
seen[1] = 1

for i in range(M):
    x = XY[i][0]
    y = XY[i][1]
    if seen[x] == 1:
        seen[y] = 1
        ball_list[x] -= 1
        ball_list[y] += 1
        if ball_list[x] == 0:
            seen[x] = 0
    else:
        ball_list[x] -= 1
        ball_list[y] += 1

print(seen.count(1))