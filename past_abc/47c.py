S = input()
count = 0
state = S[0]
for i in S[1:]:
    if i != state:
        count += 1
        state = i
print(count)