A, B, X = map(int, input().split())

D = 1
for i in range(1,19):
    if A * (10**i) + B * i < X:
        D = i + 1
    else:
        break

X -= B * D
ans = X // A

if ans == -1:
    print(0)
elif ans >= 1000000000:
    print(1000000000)
else:
    print(ans)