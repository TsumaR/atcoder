K = int(input())
S = list(input())

if len(S) <= K:
    print("".join(S))
else:
    ans = "".join(S[0:K])
    ans = ans + "..."
    print(ans)