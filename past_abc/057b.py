N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = [list(map(int, input().split())) for _ in range(M)]


for a in A:
    distance = 10**9
    point = 0
    for i, c in enumerate(C):
        if abs(a[0] - c[0]) + abs(a[1] - c[1]) < distance:
            distance = abs(a[0] - c[0]) + abs(a[1] - c[1])
            point = i
    print(point + 1)