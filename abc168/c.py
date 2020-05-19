import math
A, B, H, M = map(int, input().split())

a = 30 * (H%12) + 0.5 * M
b = 6 * M

degree = min(abs(a-b), 360 - abs(a-b))
ans = A**2 + B ** 2 - 2*A*B*math.cos(math.radians(degree))


print(ans**0.5)
