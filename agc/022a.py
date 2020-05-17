S = list(input())

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

if "".join(S) == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

ans = []

"""
多彩じゃない入力に対処できるコードを書いてしまった
"""

# 全ての文字をまだ使っていない時
for i in abc:
    if i not in S:
        S.append(i)
        print("".join(S))
        exit()

# 後ろから見て自分より辞書順で後ろのやつが，前にいなければそいつに書き換える
for i, s in enumerate(reversed(S)):
    ind = abc.index(s)
    t = abc[ind+1:]
    for j in t:
        if j not in S[0:26-i+1]:
            S[26-i-1] = j
            print("".join(S[0:26-i]))
            exit()