N = int(input())
A = list(map(int, input().split()))

before_turn = []
for i in reversed(A[1::2]):
    before_turn.append(i)

for i in A[::2]:
    before_turn.append(i)


if N % 2 == 0 or N == 1:
    print(" ".join(map(str, before_turn)))
else:
    turn = before_turn[::-1]
    print(" ".join(map(str, turn)))

"""
上記コードはこれだけ簡単に書くことができる。
evenとoddの判定を後ろでもやるのだから，最初に一気にやってあげた方が言いに決まっている。

import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
if n%2:
    print(" ".join(map(str, a[::-1][::2] + a[1::2])))
else:
    print(" ".join(map(str, a[::-1][::2] + a[::2])))
"""