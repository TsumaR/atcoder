N, K, S = map(int, input().split())

if S == 10**9:
    ans = [1]*N
else:
    ans = [S+1] * N
for i in range(K):
    ans[i] = S

print(" ".join(map(str, ans)))