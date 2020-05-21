N, Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]

sum_ac = [0] * N
count = 0
for i in range(1, N):
    if S[i-1] == "A" and S[i] == "C":
        count += 1
    sum_ac[i] = count

for l,r in LR:
    print(sum_ac[r-1] - sum_ac[l-1])