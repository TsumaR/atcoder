N = int(input())
S = input()
T = input()

if S == T:
    print(N)
    exit()
for i in reversed(range(N)):
    if S[N-i-1:] == T[:i+1]:
        print(2*N - i - 1)
        exit()
    else:
        continue

print(2*N)