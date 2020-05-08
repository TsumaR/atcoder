import itertools

N = int(input())
A = [input() for _ in range(N)]

C = [0, 0, 0, 0, 0]

for i in range(N):
    a = A[i]
    if a.startswith('M'):
        C[0] += 1
    elif a.startswith('A'):
        C[1] += 1
    elif a.startswith('R'):
        C[2] += 1
    elif a.startswith('C'):
        C[3] += 1
    elif a.startswith('H'):
        C[4] += 1

total = 0
for c in itertools.combinations(C, 3):
    total += c[0] * c[1] * c[2]

print(total)