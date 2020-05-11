# 高橋くん以外の国会議員 N <= 12
"""
最大くりーく問題
NP困難
全探索するしかない
"""
import itertools

N, M = map(int, input().split())

R = [list(map(int, input().split())) for _ in range(M)]

# 友人関係をmapにいれる
friend_map = [[0] * N for _ in range(N)]
for i in range(M):
    x, y = R[i]
    friend_map[x-1][y-1] = 1
    friend_map[y-1][x-1] = 1

ans = 0
# 全探索
for i in range(1, 1 << N):
    # 選ばれた人をいれるリスト
    group = []
    for j in range(N):
        if (i >> j) & 1:
            group.append(j)
    
    # group内で知り合いじゃないのがいたらはじくためのループ
    flag = True

    # group内から2人選ぶ組み合わせのループ
    for j in itertools.combinations(group, 2):
        if friend_map[j[0]][j[1]] == 0:
            flag = False
            break
    if flag:
        ans = max(ans, len(group))

print(ans)



# print(friend_map)
# ans = 0
# for l in friend_map:
#     ans = max(ans, sum(l) + 1)

# print(ans)