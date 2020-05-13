from math import gcd

ax, ay = map(int, input().split())
bx, by = map(int, input().split())

x = abs(ax - bx)
y = abs(ay - ax)

g = gcd(x, y)
print(g-1)