N = int(input())
K = int(input())

display = 1
for i in range(N):
    if display + K <= 2 * display:
        display += K
    else:
        display *= 2

print(display)