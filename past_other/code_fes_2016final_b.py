N = int(input())
k = 0
ans = 0
while N >= ans:
    k += 1
    ans = k * (k+1) / 2

exit_num = int(k * (k+1) / 2 - N)
for i in range(1,k+1):
    if i != exit_num:
        print(i)