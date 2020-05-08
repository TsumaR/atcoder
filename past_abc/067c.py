N = int(input())
A = list(map(int, input().split()))
arai = sum(A)
sunuke = 0

ans = 10**10
for i in range(0, N-1):
    sunuke += A[i]
    arai -= A[i]
    ans = min(ans, abs(sunuke - arai))

print(ans)