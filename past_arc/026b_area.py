"""
約数の数を素数要素の面積のように考える方法
素因数分解を利用して解く解法

ただしN <= 10**10の条件下でTLE
"""
from collections import Counter
N = int(input())

# 素数を求める関数
def factorize(n):
    factorys = []
    rest_num = n
    i = 2
    while rest_num > 1:
        if rest_num % i == 0:
            factorys.append(i)
            rest_num //= i
        else:
            i += 1
    return factorys

arr = Counter(factorize(N))

ans = 1
for k, v in arr.items():
    temp = 0
    for i in range(v+1):
        temp += k**i
    ans *= temp

sum_div = ans - N 
if sum_div == N:
    print("Perfect")
elif sum_div < N:
    print("Deficient")
else:
    print("Abundant")