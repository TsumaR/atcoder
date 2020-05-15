count = 0
S = [int(i) for i in list(input())]

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        if S[i] == 0:
            S[i+1] = 1
        elif S[i] == 1:
            S[i+1] = 0
        count += 1 
print(count)