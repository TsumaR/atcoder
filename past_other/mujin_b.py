import math

a, b, c = map(int , input().split())

M = (a+b+c)**2 * math.pi

if a + b > c and b + c > a and c + a > b:
    print(M)
else:
    l = min(abs(a - (c-b)), abs(a- (c+b)) , abs(a- (b-c)))
    print(M - l**2 * math.pi)
