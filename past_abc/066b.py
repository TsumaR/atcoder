S = input()
for i in reversed(range(len(S)-1)):
    if i %2 == 0:
        continue
    else:
        if S[0:i//2] == S[i//2+1:i]:
            print(i+1)
            break