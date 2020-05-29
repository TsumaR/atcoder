A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]

result = [[0]*3 for _ in range(3)]

for b in B:
    for i in range(3):
        for j in range(3):
            if b == A[i][j]:
                result[i][j] = 1

for h in result:
    if 0 not in h:
        print("Yes")
        exit()

for i in range(3):
    if result[0][i] == result[1][i] == result[2][i] == 1:
        print("Yes")
        exit()

if result[0][0] == result[1][1] == result[2][2] == 1:
    print("Yes")
    exit()

if result[0][2] == result[1][1] == result [2][0] == 1:
    print("Yes")
    exit()

print("No")