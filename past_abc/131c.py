a, b, c, d = map(int, input().split())

"""
両方に関して割り切れるものの個数から公倍数で割り切れるものを除けばいい
"""
import fractions

C = b//c - (a-1)//c
D = b//d - (a-1)//d

# 最小公倍数を求める
CD = fractions.gcd(c, d)
lcm = (c * d) // CD

G = b//lcm - (a-1)//lcm


count = C + D - G
print(b - a + 1 - count)