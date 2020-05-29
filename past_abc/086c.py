N = int(input())
T = [0] * N
XY = [0] * N
for i in range(N):
    t,x,y = map(int, input().split())
    T[i] = t
    XY[i] = [x,y]

x,y = 0,0
t = 0
for i in range(N):
    nx,ny = XY[i]
    nt = T[i]
    distance = abs(x-nx) + abs(y-ny)
    if distance <= nt - t and ((nt - t) - distance) %2 == 0:
        x,y = nx,ny
        t = nt
    else:
        print("No")
        exit()

print("Yes")