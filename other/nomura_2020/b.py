T = list(input())
for i, s in enumerate(T):
    if s == "?":
        T[i] = "D"

print("".join(T))