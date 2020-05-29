N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

result = [0] * N

relation = [[0] * (N+1) for _ in range(N+1)]
for a,b in AB:
    relation[a][b] = 1
    relation[b][a] = 1
for c,d in CD:
    relation[c][d] = -1
    relation[d][c] = -1

def dfs(s):
    relation[s]