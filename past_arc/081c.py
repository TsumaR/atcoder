from collections import Counter
N = int(input())
A = list(map(int, input().split()))

C = sorted(Counter(A).items(), reverse = True)

edge = []
for k,v in C:
    if len(edge) >=2:
        break
    if v >= 2:
        for _ in range(v // 2):
            edge.append(k)
if len(edge) <= 1:
    print(0)
    exit()
print(edge[0] * edge[1])