S = list(input())
L = len(S)
key = list("keyence")

for i in range(0,8):
    if S[0:i] == key[0:i] and S[L-7+i:] == key[i:]:
        print("YES")
        exit()
print("NO")