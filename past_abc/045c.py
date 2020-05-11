"""
abc167でC問題にてbit全探索を解けなかったので猛省
"""

N = list(input())

L = len(N)
ans = 0

for i in range(0, 1 << L-1):
    s = []
    minus = [N[0]]
    for j in range(L-1):
        if (i >> j) & 1:
            s.append(int("".join(minus)))
            minus = [N[j+1]]
        else:
            minus.append(N[j+1])
    s.append(int("".join(minus)))
    ans += sum(s)
print(ans)