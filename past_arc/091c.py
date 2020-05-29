N, K = map(int, input().split())
if N >= 3 and K >= 3:
    print((N-2)*(K-2))
elif N == 1 or K == 1:
    ans = max(N, K) - 2
    if ans >= 0:
        print(ans)
    else:
        print(1)
else:
    print(0)
