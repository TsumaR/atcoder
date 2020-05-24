N = int(input())
D = list(map(int, input().split()))
D.sort()
M = int(input())
T = list(map(int, input().split()))
T.sort()

while len(T) > 0:
    t = T.pop()
    flag = True
    while flag:
        if len(D) <= 0:
            print("NO")
            exit()
        d = D.pop()
        if d == t:
            flag = False
        elif d < t:
            print("NO")
            exit()
        else:
            continue

print("YES")