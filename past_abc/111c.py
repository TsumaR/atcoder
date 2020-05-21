from collections import Counter

N = int(input())
V = list(map(int, input().split()))

if len(set(V)) == 1:
    print(len(V)//2)
    exit()

V_odd = [i for i in V[::2]]
V_even = [i for i in V[1::2]]
V_odd_counter = Counter(V_odd)
V_even_counter = Counter(V_even)

vodd = V_odd_counter.most_common()
veven = V_even_counter.most_common()
vlen = len(V)
while True:
    if vodd[0][0] != veven[0][0]:
        print(vlen - vodd[0][1] - veven[0][1])
        exit()
    else:
        print(min(vlen - vodd[1][1] - veven[0][1],
                    vlen - vodd[0][1] - veven[1][1]))
        exit()