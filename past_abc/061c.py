from collections import OrderedDict
result = OrderedDict()
N, K = map(int, input().split())
for i in range(N):
    a,b = map(int, input().split())
    if a in result:
        result[a] += b
    else:
        result[a] = b

result = sorted(result.items())
for k,v in result:
    if K > v:
        K -= v
    else:
        print(k)
        exit()