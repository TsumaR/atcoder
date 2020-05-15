"""
十分に小さい
"""

N = int(input())
S = [list(input()) for _ in range(N)]
reversed_S = []
for i in range(N):
    reversed_S.append(S[i][::-1])

reversed_S.sort()
for i in reversed_S:
    print("".join(i[::-1]))