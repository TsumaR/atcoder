# 常にi < jを考える
# これだとTLE

N = int(input())
H = [0]
H.extend(list(map(int, input().split())))

plus = [H[i] + i for i in range(1,N+1)]
minus = [i - H[i] for i in range(1, N+1)]

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        if plus[i] == minus[j]:
            cnt += 1

print(cnt)