N, K = map(int, input().split())
R, S, P = list(map(int, input().split()))
T = list(input())

result = [0] * N
for i,t in enumerate(T):
    if t == "r":
        result[i] = P
    elif t == "s":
        result[i] = R
    else:
        result[i] = S

for i in range(K, N):
    if result[i] == result[i-K]:
        result[i] = 0

print(sum(result))