N, K = map(int, input().split())


for i in range(1,N):
    if N > K**i:
        continue
    elif N == K**i:
        print(i+1)
        exit()
    else:
        print(i)
        exit()
print(1)