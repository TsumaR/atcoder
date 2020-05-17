"""
3*10**5
単純に両側の差を全探索だと間に合わないO(N*2)

情報を先に保存しておきそれを使う
"""

N = int(input())
S = input()

E_list = [0] * N 
W_list = [0] * N

n = 0
for i in range(1,N):
    if S[i-1] == "W":
        n += 1
        W_list[i] = n
    else:
        W_list[i] = n

n = 0
for i in reversed(range(N-1)):
    if S[i+1] == "E":
        n += 1
        E_list[i] = n
    else:
        E_list[i] = n

print(min([e+w for e,w in zip(E_list, W_list)]))