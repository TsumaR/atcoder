# 隣二つ影響しか受けない

N = int(input())
A = list(map(int, input().split()))

M = 0
for i in reversed(A[::2]):
    M += i

for i in reversed(A[1:N:2]):
    M -= i
ans = [0] * N
ans[0] = M

for i in range(1,N):
    ans[i] = 2 * (A[i-1] - ans[i-1] // 2)

print(" ".join(map(str, ans)))