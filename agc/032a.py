N = int(input())
B = list(map(int, input().split()))

ans = [0] * N
for i in range(N):
    for j in reversed(range(len(B))):
        if j == B[j] - 1:
            ans[i] = B[j]
            if len(B) > 0:
                B.pop(j)
            break

if 0 in ans:
    print(-1)
else:
    for i in ans[::-1]:
        print(i)