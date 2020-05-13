import itertools

N = int(input())
l = ['a', 'b', 'c']

ans = []
def dfs(s):
    if len(s) == N:
        ans.append(s)
        return
    else:
        for i in range(3):
            t = s + l[i]
            dfs(t)

dfs('')
ans.sort()
for s in ans:
    print(s)