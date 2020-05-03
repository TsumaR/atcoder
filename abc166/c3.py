N, M = map(int, input().split())
H = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]



graph = [[] for _ in range(N+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

ans = []

for i in range(1,N+1):
    can = graph[i]
    hights = []
    for j in can:
        hights.append(H[j-1])
    if len(hights) == 0:
        ans.append(i)
    else:
        h = max(hights)
        if H[i-1] > h:
            ans.append(i)

print(len(set(ans)))