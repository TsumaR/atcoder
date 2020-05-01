from collections import deque

N = int(input())
D = [int(input()) for _ in range(N)]
tower = []

def stacking(box, tower):
    if tower == [] or box > max(tower):
        tower.append(box)
    else:
        tower.sort()
        for i in range(len(tower)):
            if tower[i] >= box:
                tower[i] = box
                break
                
    return tower

for j in range(N):
    box = D[j]
    stacking(box, tower)

print(len(tower))