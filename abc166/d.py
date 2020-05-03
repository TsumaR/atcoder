x = int(input())

# for i in range(400):
#     for j in range(i - 800, i):
#         if i ** 5 - j ** 5 == x:
#             print(i, j)
#             exit()
for i in range(-118,120):
    for j in range(-118, i+1):
        if i ** 5 - j ** 5 == x:
            print(i, j)
            exit()
