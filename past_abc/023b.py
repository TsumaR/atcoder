"""
Sの長さは１００以下
"""

N = int(input())
S = list(input())

if S[N//2] != 'b':
    print(-1)
    exit()
if N%2 == 0:
    print(-1)
    exit()


for i in range(N-1):
    if S[i] == 'a' and S[i+1] == 'b':
        continue
    elif S[i] == 'b' and S[i+1] == 'c':
        continue
    elif S[i] == 'c' and S[i+1] == 'a':
        continue
    else:
        print(-1)
        exit()
print(N//2)