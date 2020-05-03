import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N-1)]
process = [list(map(int, input().split())) for _ in range(Q)]

graph = [[] for _ in range(N+1)]
value = [0] * (N + 1)

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for que in process:
    value[que[0]] += que[1]

def dfs(s, parent, add):
    value[s] += add
    for x in graph[s]:
        if x == parent:
            continue
        dfs(x, s, value[s])

dfs(1, 0, 0)

ans =  ' '.join(map(str, value[1:]))

print(ans)