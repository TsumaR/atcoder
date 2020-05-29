S = list(input())
ln = len(S)
next_lr = [0] * ln
next_r = 0
next_l = 0


for i in range(ln):
    if S[i] == "R":
        next_r = i
        if i < next_l:
            next_lr[i] = next_l - i
        else:
            for j in range(i+1,ln):
                if S[j] == "L":
                    next_l = j
                    next_lr[i] = j - i
                    break
    else:
        next_lr[i] = next_r - i


result = [0] * ln
for i in range(ln):
    nx = next_lr[i]
    if nx %2 == 0:
        result[i+nx] += 1
    elif nx > 0:
        result[i+nx-1] += 1
    else:
        result[i+nx+1] += 1

print(" ".join(map(str, result)))
