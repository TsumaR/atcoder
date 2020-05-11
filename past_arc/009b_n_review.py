import numpy as np
import copy

B = list(map(int, input().split()))
N = int(input())
A = list(int(input()) for _ in range(N))
A_cp = copy.deepcopy(A)

# 1数字ずつ，前から数字を置き換えている

BR = [0] * 10

for i, n in enumerate(B):
    BR[n] = i

for i, n in enumerate(A_cp):
    s = [int(d) for d in str(n)]
    for j, m in enumerate(s):
        s[j] = BR[m]
    A_cp[i] = int("".join(map(str, s)))

A_cp = np.array(A_cp)
indexs = A_cp.argsort()

for i in indexs:
    print(A[i])


# b = list(map(int,input().split()))
# d = {}
# for i in range(10):d[b[i]] = i
# n = int(input())
# l = [[0,0] for _ in range(n)]
# for i in range(n):
#     a = input()
#     t = ""
#     for c in a:
#         x = int(c)
#         t += str(d[x])
#     l[i] = [int(t),a]
# l.sort()
# for i in range(n):
#     print(l[i][1])
