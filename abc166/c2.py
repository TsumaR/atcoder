N, M = map(int, input().split())
H = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

seen = [0] * (N+1)

def dfs(x):
    if seen[x] == 1:
        return
    else:
        seen[x] = 1
        for i in graph[x]:
            dfs(i)

ans = 0
for i in range(1,N+1):
    if seen[i] == 0:
        print(i)
        print(seen)
        ans += 1
        dfs(i)
print(ans)