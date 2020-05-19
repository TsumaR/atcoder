N = list(input())
if len(N) == 1:
    n = int(N[0])
else:
    n = int(N[-1])

if n == 2 or n == 4 or n == 5 or n == 7 or n == 9:
    print("hon")
elif n == 0 or n == 1 or n == 6 or n == 8:
    print("pon")
elif n == 3:
    print("bon")
