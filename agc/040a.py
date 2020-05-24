S = list(input())
result = [0] * (len(S)+1)
count = 0
for i,s in enumerate(S):
    if s == ">":
        result[i+1] = result[i] - 1
    else:
        result[i+1] = result[i] + 1

print(result)
min_num = min(result)
print(sum(result))
print(sum(result) + len(S) * (0 - min_num))