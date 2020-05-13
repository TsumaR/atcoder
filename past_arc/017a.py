"""
素数判定
短いので全て回せばいい
"""

N = int(input())
#　平方根まででループを回す
for i in range(2, int((N**0.5)) + 1):
    if N % i == 0:
        print("NO")
        exit()
print("YES")