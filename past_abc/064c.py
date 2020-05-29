N = int(input())
A = list(map(int, input().split()))

silver = 0
rate = set([])
for a in A:
    if a >= 3200:
        silver += 1
    elif 2800 <= a <= 3199:
        rate.add("red")
    elif 2400 <= a <= 2799:
        rate.add("orange")
    elif 2000 <= a <= 2399:
        rate.add("yellow")
    elif 1600 <= a <= 1999:
        rate.add("blue")
    elif 1200 <= a <= 1599:
        rate.add("cyan")
    elif 800 <= a <= 1199:
        rate.add("green")
    elif 400 <= a <= 799:
        rate.add("brown")
    else:
        rate.add("hai")

if len(rate) == 0:
    print(1, silver)
else:
    print(len(rate), len(rate)+silver)