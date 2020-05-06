N, K = map(int, input().split())

if N < K:
    print(min(N, K-N))
    exit()
else:
    wari = N // K
    print(min(N - (K * wari), K * (wari + 1) - N))