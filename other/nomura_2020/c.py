N = int(input())
A = list(map(int, input().split()))

if A[0] == 1 and N == 0:
    print(1)
    exit()

if A[0] >= 1:
    print(-1)
    exit()

# 根から見たときにあり得る各層最大の要素数
max_leaf = [0] * (N + 1)
max_leaf[0] = 1
leaf = 1
for i in range(N):
    leaf = 2 * (leaf - A[i]) 
    if leaf < 0:
        print(-1)
        exit()
    max_leaf[i+1] = leaf

result = [0] * (N+1)
result[N] = A[N]
for i in reversed(range(N)):
    if result[i+1] + A[i] <= max_leaf[i]:
        result[i] = result[i+1] + A[i]
    elif -(-result[i+1] // 2) > max_leaf[i]:
        print(-1)
        exit()
    else:
        result[i] = max_leaf[i]

print(sum(result))
