C = int(input())
box = [0, 0, 0]
for _ in range(C):
    b = list(map(int, input().split()))
    b.sort()
    for i in range(3):
        if b[i] > box[i]:
            box[i] = b[i]
    box.sort()

print(box[0]*box[1]*box[2])