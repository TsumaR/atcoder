import bisect

N = int(input())
L = list(map(int, input().split()))

L.sort()
print(L)
ans = 0
for ai in range(N):
    for bi in range(ai+1, N):
        ci = bisect.bisect_left(L, L[ai]+L[bi])
        print(ai, bi, ci)
        if ci > bi:
            ans += ci - bi - 1
            print(ci - bi - 1)
        else:
            pass

print(ans)