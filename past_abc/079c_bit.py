S = list(input())
L = len(S)

for i in range(0, 1 << L-1):
    f = S[0]
    ans = int(S[0])
    for j in range(L-1):
        if (i >> j) & 1:
            f += "+"
            f += S[j+1]
            ans += int(S[j+1])
        else:
            f += "-"
            f += S[j+1]
            ans -= int(S[j+1])
    if ans == 7:
        print(f, "=7", sep="")
        exit()