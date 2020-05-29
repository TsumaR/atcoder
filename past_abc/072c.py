from collections import Counter
N = int(input())
A = list(map(int, input().split()))

result_list = []
for a in A:
    result_list.append(a-1)
    result_list.append(a)
    result_list.append(a+1)
C = Counter(result_list).most_common()
print(C[0][1])