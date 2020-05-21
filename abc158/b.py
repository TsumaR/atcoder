N, A, B = map(int, input().split())
S = A + B
count = N//S * A
if N%S >= A:
    count += A
else:
    count += N%S

print(count)