n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

sum_ab = len(A & B)
union_ab = len(A | B)

print(sum_ab / union_ab)