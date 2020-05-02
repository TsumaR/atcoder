import copy

n, m, q = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(q)]

B = []

# 再帰,全探索
def dfs(A, l):
    if l == n:
        B.append(A)
    else:
        for i in range(A[-1], m+1):
            nA = copy.copy(A)
            nA.append(i)
            dfs(nA, l+1)
dfs([1],1)

print(B)
