T = int(input())

for t in range(T):
    S = input()
    count = 0
    position = 0
    while position < len(S) - 4:
        if S[position:position + 5] == "tokyo" or S[position:position + 5] == "kyoto":
            count += 1
            position += 5
        else:
            position += 1
    print(count)


