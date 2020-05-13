W, H, x, y = map(int, input().split())

"""
直方体は中身を通る線で半分に割ることができる
"""

if W/2 == x and H/2 == y:
    print(W * H / 2, 1)
else:
    print(W * H / 2, 0)