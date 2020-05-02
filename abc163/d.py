import itertools

N = int(input())
S = input()

# R = [i for i, x in enumerate(S) if x == "R"]
# G = [i for i, x in enumerate(S) if x == "G"]
# B = [i for i, x in enumerate(S) if x == "B"]

# RGB = list(itertools.product(R,G, B))
# print(RGB)

# result = 0
# for item in RGB:
#     s_item = sorted(item)
#     if s_item[2] - s_item[1] != s_item[1] - s_item[0]:
#         result += 1

# print(result)

r_cnt = S.count("R")
g_cnt  = S.count("G")
b_cnt = S.count("B")

ans = r_cnt * g_cnt * b_cnt

for i in range(N):
    for d in range(N):
        j = i + d
        k = j + d
        if k >= N:
            break
        if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            ans -= 1
print(ans)
