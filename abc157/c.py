N, M = map(int, input().split())
result = [0] * N

for i in range(M):
    s,c = map(int, input().split())
    if s == 1 and c == 0 and N != 1:
        print(-1)
        exit()
    if result[s-1] != 0 and result[s-1] != c:
        print(-1)
        exit()
    else:
        result[s-1] = c

if len(result) >= 2 and result[0] == 0:
    result[0] = 1

print("".join(map(str, result)))