N = int(input())
A = [int(input()) for _ in range(N)]

result = set([])
for i in A:
    if i in result:
        result.remove(i)
    else:
        result.add(i)
print(len(result))