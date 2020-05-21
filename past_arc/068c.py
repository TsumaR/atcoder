"""
10**15なので，ループで割ることを考える
1 + (6, 5)
"""

x = int(input())
count = (x // 11) * 2
x = x % 11
if x > 6:
    print(count+2)
elif x > 0:
    print(count+1)
else:
    print(count)