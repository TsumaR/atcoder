from collections import deque

A = deque(list(input()))
B = deque(list(input()))
C = deque(list(input()))

def extract(s):
    if s == "a":
        S = A
    if s == "b":
        S = B
    elif s == "c":
        S = C
    if len(S) == 0:
        print(s.upper())
        exit()
    t = S.popleft()
    extract(t)

extract("a")
print("s")