import fractions
N, M = map(int, input().split())
S = input()
T = input()

G = N * M // fractions.gcd(N, M)
slist = [i*(G//N) for i in range(N)]
mlist = [i*(G//M) for i in range(M)]
sm = set(slist) & set(mlist)
for i in sm:
    si = slist.index(i)
    mi = mlist.index(i)
    if S[si] != T[mi]:
        print(-1)
        exit()

print(G)