x, y, r = map(int, input().split())
a, b, c, d = map(int, input().split())

xy = [[a, b], [a, b+d], [a+c, b], [a+c, b+d]]

if xy[0][0] < x < xy[2][0] and xy[0][1] < y < xy[1][1]:
    if x - r >= a and x + r <= a+c and y - r >= b and y + r <= b + d:
        print("NO")
        print("YES")
        exit()
    else:
        print("YES")
        print("YES")
        exit()
else:
    for i in range(4):
        top_point = xy[i]
        if (top_point[0] - x)**2 + (top_point[1] - y)**2 > r**2:
            print("YES")
            print("YES")
            exit()

print("YES")
print("NO")

