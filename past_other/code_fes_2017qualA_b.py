N, M, K = map(int, input().split())

for l in range(N+1):
    for k in range(M+1):
        if (N-l)*(M-k) + l*k == K:
            print("Yes")
            exit()
print("No")