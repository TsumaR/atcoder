import math

a, b, x = map(int, input().split())

"""
a<=100
b<=100
x<=a**2*b

角度y傾けた時の空白の体積を求めれば良い
"""

rest = a**2 * b - x
if rest <= x:
    c = (rest * 2) / a**2
    print(math.degrees(math.atan2(c, a)))
else:
    c = (x * 2) / (a*b)
    print(90 - math.degrees(math.atan2(c, b)))