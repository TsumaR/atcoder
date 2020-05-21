A, B = map(int ,input().split())

n = (100/8) * 100
for i in range(int(n)):
    if int(i*0.08) == A and i//10 == B:
        print(i)
        exit()
print(-1)
