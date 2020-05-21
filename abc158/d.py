S = list(input())
N = int(input())

Q = [list(input().split()) for _ in range(N)]

count = 0
c = 0

ans_append = []
ans_insert = []

for q in Q:
    if q[0] == "1":
        count += 1
        c = count % 2
    else:
        if (c == 0 and q[1] == "1") or (c == 1 and q[1] == "2"):
            ans_insert.append(q[2])
        elif (c == 0 and q[1] == "2") or (c == 1 and q[1] == "1"):
            ans_append.append(q[2])


if count % 2  == 1:
    ans = ans_append[::-1] + S[::-1] + ans_insert
    print("".join(ans))
else:
    ans = ans_insert[::-1] + S + ans_append
    print("".join(ans))