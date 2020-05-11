N = int(input())
A = list(map(int, input().split()))

s, r, ans = 0, 0, 0

for i in range(N-1):
    if r >= i and r != 0:
        ans += r - i + 1
    else:
        r = i
        while r < N-1 and A[r+1] > A[r]:
            r += 1
        ans += r - i + 1
print(ans)