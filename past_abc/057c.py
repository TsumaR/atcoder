"""
master of 整数
素因数分解
https://qiita.com/drken/items/a14e9af0ca2d857dad23
"""

N = int(input())
ans = len(str(N))
for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        f_ab = max(len(str(i)), len(str(N//i)))
        ans = min(f_ab, ans)

print(ans)