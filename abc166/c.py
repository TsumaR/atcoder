N, M = map(int, input().split())
H = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N+1)]
for edge in edges:
    graph[edge[0]].append(edge[1])
print(graph)

candidate = list(range(1,N+1))

ans = 0
while max(H) != 0:
    h = [i+1 for i, v in enumerate(H) if v == max(H)]
    for i in h:
        H[i-1] = 0
        if i not in candidate:
            break
        else:
            print(i)
            ans += 1
            print(ans)
            g = graph[i]
            for j in g:
                if j in candidate:
                    candidate.remove(j)
print(ans)