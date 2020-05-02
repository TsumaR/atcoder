import math
X = int(input())

A = 100
count = 0
while A < X:
    A = math.floor(A * 1.01)
    count += 1
print(count)


# math.floorをする必要はなく，int()でよかったらしい

# 1.01翔の気持ち悪いから A += A // 100
# とかがよかったかもしれない
