"""
マスターオブ整数
公約数の問題
公約数とは最大公約数の約数であるという性質がある

大事なのは公約数が最大公約数の約数であること
"""
import fractions
A, B = map(int, input().split())

# まず公約数を列挙したくなる
# 最大公約数を求めてその約数を列挙する
# 最大公約数はユークリッドの互除法で求めることができる

ans = 1
gcd_value = fractions.gcd(A, B)
for i in range(2, int(gcd_value**0.5) + 1):
    if gcd_value % i == 0:
        ans += 1
        while gcd_value % i == 0:
            gcd_value //= i

# divisorリストの中からどの二つ互いに素となるようにいくつか選ぶ
# 素因数の数+1を答えれば良い
if gcd_value != 1:
    ans += 1

print(ans)