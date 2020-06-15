X, N = map(int, input().split())
P = set(list(map(int ,input().split())))

for i in range(200):
    if X-i not in P:
        print(X-i)
        exit()
    elif X+i not in P:
        print(X + i)
        exit()
    else:
        continue

print(X)