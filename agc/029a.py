S = list(input())
ans = 0
# 復習よう
while True:
    count = 0
    for i in range(0, len(S)-1):
        if S[i] == "B" and S[i+1] == "W":
            count += 1
            S[i] = "W"
            S[i+1] = "B"
    if count > 0:
        ans += count
    else:
        print(ans)
        exit()