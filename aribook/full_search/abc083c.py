X, Y = map(int, input().split())
a = 0
metar = True
while metar:
    c = X * (2 ** a)
    if c <= Y:
        a += 1
    else:
        metar = False
print(a)