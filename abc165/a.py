K = int(input())
A, B = map(int, input().split())

A_w = A // K
A_a = A % K
B_w = B // K 

if A_w == B_w and A_a != 0:
    print("NG")
else:
    print("OK")