N = int(input())
A = [int(input()) for _ in range(N)]

i = 1
count = 0
find = False
for _ in range(N):
    count += 1
    i = A[i-1]
    if i == 2:
        find = True
        break

if find:
    print(count)
else:
    print(-1)