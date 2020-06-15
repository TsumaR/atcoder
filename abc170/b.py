X, Y = map(int, input().split())
maxX = X * 4
minX = X * 2
if Y %2 == 0 and minX <= Y <= maxX:
    print("Yes")
else:
    print("No")