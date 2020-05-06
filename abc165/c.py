N, M, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(Q)]


result = []


point = 0

def dfs(x):
    point = 0
    distance = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1}
    for item in A:
        # if x == item[0] and item[1] == M and distance + item[2] <= M:
        #     point += item[3]    
        #     result.append(point)
        #     break
        if x == item[0]:
            distance[item[1]] = distance[x] + item[2]
            if distance[item[1]] <= M:
                point += item[3]

        # elif x == item[0] and distance + item[2] > M:
        #     break
        # else:
        #     break
    return point

dfs(1)
print(point)
