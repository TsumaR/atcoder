N = int(input())
X = list(map(int, input().split()))

XX = sorted(X)
before = XX[N//2 -1]
after = XX[N//2]

for i in X:
    if i <= before:
        print(after)
    else:
        print(before)