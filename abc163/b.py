N, M = map(int, input().split())
A = list(map(int, input().split()))

whole_day = N - sum(A)

if whole_day >= 0:
    print(whole_day)
else:
    print(-1)
