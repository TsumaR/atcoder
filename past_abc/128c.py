N, M = map(int, input().split())
light = [0] * M
switch = []
for i in range(M):
    ks = list(map(int, input().split()))
    light[i] = ks[0]
    switch.append(ks[1:])
P = list(map(int, input().split()))

count = 2 ** N
for i in range(2 ** N):
    switch_state = [0] * N
    for j in range(N):
        if ((i >> j) & 1):
            switch_state[j] = 1
    for m in range(M):
        point = 0
        for s in switch[m]:
            point += switch_state[s-1]
        if point %2 != P[m]:
            count -= 1
            break
print(count)