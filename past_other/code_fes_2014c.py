A, B = map(int , input().split())

b_uruu = B//4 - B//100 + B//400
a_uruu = (A-1)//4 - (A-1)//100 +(A-1)//400

print(b_uruu - a_uruu)