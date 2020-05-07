N = int(input())
K = [list(map(int, input().split())) for _ in range(N)]
K.sort(key=lambda x: x[1])

M = 0
for k,v in K:
    M += k
    if M > v:
        print("No")
        exit()

print("Yes")