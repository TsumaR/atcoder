N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    graph[i][i] = i

for a,b in AB:
    graph[a][b] = b
    graph[b][a] = a

for i in range(1,N+1):
    count = []
    g = graph[i]
    for j in range(1, N+1):
        if g[j] != 0:
            count.extend(graph[j])
    ans = set(count) - set(g)
    print(len(ans))