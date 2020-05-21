L, X, Y, S, D = map(int, input().split())

if D >= S:
    positive = D - S
    negative = L - positive
else:
    negative = S - D
    positive = L - negative

if Y > X:
    print(min(positive/(X+Y), negative/(Y-X)))
else:
    print(positive/(X+Y))