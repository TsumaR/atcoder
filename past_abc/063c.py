N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
sum_score = sum(S)
if sum_score %10 != 0:
    print(sum_score)
    exit()
else:
    for s in S:
        if s %10 != 0:
            print(sum_score - s)
            exit()
        else:
            continue

print(0)