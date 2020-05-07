S = input()
N = len(S)

a_ = int((N-1)//2)
b_ = int((N+3)//2 -1)
a = S[:a_]
b = S[b_:N+1]

if S == S[::-1] and a == a[::-1] and b == b[::-1]:
    print('Yes')
else:
    print('No')