N, M = map(int, input().split())
# まず，変換しないで行けるやつをできるだけ
if M >= 2*N:
    M -= 2*N
    print(N + M//4)
else:
    print(M//2)
