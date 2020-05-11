import itertools

N, M, X = map(int, input().split())
C = []; A = []; T = []
for _ in range(N):
    s = list(map(int, input().split()))
    T.append(s)


comb = []

for i in range(1,N+1):
    comb.append(list(itertools.combinations(T, i)))

comb = itertools.chain.from_iterable(comb)
count = []

for j in comb:
    t = [0, 0, 0, 0]
    for k in range(len(j)):
        t[0] += j[k][0]
        t[1] += j[k][1]
        t[2] += j[k][2]
        t[3] += j[k][3]
    count.append(t)

count.sort()


for i in count:
    if min(i[1:]) >= X:
        print(i[0])
        exit()

print(-1)

