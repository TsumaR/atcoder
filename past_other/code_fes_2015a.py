N, T = map(int, input().split())
dif_ab = [0]*N

sum_a = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    dif_ab[i] = tmp[0] - tmp[1]
    sum_a += tmp[0]
if sum_a - sum(dif_ab) > T:
    print(-1)
    exit()
count = 0
dif_ab.sort()
while sum_a > T:
    count += 1
    sum_a -= dif_ab.pop()

print(count)