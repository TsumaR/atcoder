import math
a, b, c = map(int, input().split())
if 2*(a*b + (a+b)*c) < a**2+b**2+c**2 and c > a + b:
    print('Yes')
else:
    print('No')