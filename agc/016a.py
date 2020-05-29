from collections import Counter
S = list(input())
abc = [chr(ord('a') + i) for i in range(26)]

ans = 100000
for s in abc:
    result = S
    count = 0
    while len(set(result)) > 1:
        count += 1
        tmp = ["dd"] * (len(result) - 1)
        for i in range(len(result)-1):
            if result[i] == s or result[i+1] == s:
                tmp[i] = s
            else:
                tmp[i] = result[i]
        result = tmp
    ans = min(ans, count)

print(ans)