N, M = map(int, input().split())
A = list(map(int , input().split()))
B = list(map(int , input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

if M > N:
    print("NO")
    exit()

for i in range(M):
    if A[i] < B[i]:
        print("NO")
        exit()

print("YES")
