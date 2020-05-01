import itertools

N = int(input())
k = int(input())
card = [input() for i in range(N)]

number = set()
for i in itertools.permutations(card, k):
    number.add("".join(i))

print(len(number))

