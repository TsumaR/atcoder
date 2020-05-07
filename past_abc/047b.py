W, H, N = map(int, input().split())
WL = 0
HL = 0
X = []
Y = []
A = []
for _ in range(N):
    x,y,a = map(int, input().split())
    X.append(x)
    Y.append(y)
    A.append(a)

for i in range(N):
    if A[i] == 1 and WL <= X[i]:
        WL = X[i]
    elif A[i] == 2 and W >= X[i]:
        W = X[i]
    elif A[i] == 3 and HL <= Y[i]:
        HL = Y[i]
    elif A[i] == 4 and H >= Y[i]:
        H = Y[i]

if W - WL <= 0 or H - HL <= 0:
    print(0)
    exit()

print((W - WL) * (H - HL))