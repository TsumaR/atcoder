S = list(input())
T = list(input())
L = len(S)

atcoder = ['a', 't', 'c', 'o', 'd', 'e', 'r']
for i in range(L):
    if S[i] == T[i]:
        continue
    elif S[i] == '@' and T[i] in atcoder:
        continue
    elif T[i] == '@' and S[i] in atcoder:
        continue
    else:
        print('You will lose')
        exit()

print('You can win')