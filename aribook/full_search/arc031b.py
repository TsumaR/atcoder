import copy
import itertools
import sys

A = [list(input()) for i in range(10)]

def umetate(x,y):
    if not(0 <= x < 10) or not(0 <= y < 10) or A_cop[x][y] == "x":
        return
    if A_cop[x][y] == "o":
        A_cop[x][y] = "x"
        umetate(x+1, y)
        umetate(x-1, y)
        umetate(x, y-1)
        umetate(x, y+1)


for i in range(10):
    for j in range(10):
        if A[i][j] == "x":
            A_cop = copy.deepcopy(A)
            A_cop[i][j] = "o"
            umetate(i,j)
            flat_A_copy = list(itertools.chain.from_iterable(A_cop))
            if "o" not in flat_A_copy:
                print("YES")
                sys.exit()

print("NO")
            
