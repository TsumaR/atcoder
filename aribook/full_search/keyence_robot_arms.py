N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]

# [終点，始点]のリスト
coordinate = [[i[0] + i[1], max(i[0] - i[1], 0), ] for i in R]
coordinate.sort()

ans = 0
end_point = 0

for i in range(N):
    if end_point <= coordinate[i][1]:
        ans += 1
        end_point = coordinate[i][0]

print(ans)