N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()

items = R[N-K:N]
ans = 0
for i in range(K):
    ans = (ans + items[i]) / 2
print(ans)