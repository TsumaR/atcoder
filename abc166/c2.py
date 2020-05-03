N, M = map(int, input().split())
H = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])


ans = 0
for i in range(1,N+1):
    highest = True
    for j in graph[i]:
        if H[i-1] <= H[j-1]:
            highest = False
    if highest:
        ans += 1

print(ans)