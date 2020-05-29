N = int(input())
A = list(map(int, input().split()))

mod_four = len([i for i in A if i % 4 == 0])
odd_number = len([i for i in A if i % 2 == 1])

if mod_four >= odd_number:
    print("Yes")
elif mod_four + 1 == odd_number and N - mod_four - odd_number == 0:
    print("Yes")
else:
    print("No")