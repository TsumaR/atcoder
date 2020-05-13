L, R = map(int, input().split())
if R >= L + 2019:
    R = R + 2019

ans = 2020
for i in range(L, R+1):
    for j in range(i+1, R+1):
        daaam = i * j % 2019
        if daaam == 0:
            print(daaam)
            exit()
        ans = min(daaam, ans)
print(ans)