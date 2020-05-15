N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    s = list(map(int, input().split()))
    C.append(s[0])
    A.append(s[1:])
ans = float('INF')
for i in range(0, 1 << N):
    scores = [0] * M
    count = 0
    for j in range(N):
        if (i >> j) & 1:
            for s in range(M):
                scores[s] += A[j][s]
            count += C[j]
    if min(scores) < X:
        continue
    else:
        ans = min(ans, count)

if ans == float("INF"):
    print(-1)
else:
    print(ans)