S = list(input())

abc = [chr(ord('a') + i) for i in range(26)]

if len(S) < 26:
    rest_alp = list(set(abc) - set(S))
    rest_alp.sort()
    S.append(rest_alp[0])
    print("".join(S))
    exit()
else:
    for i in reversed(range(25)):
        for j in reversed(range(i+1, 26)):
            if S[i] < S[j]:
                ans = S[:i].append(S[j])
                print("".join(S[:i]) + "".join(S[j]))
                exit()
print(-1) 