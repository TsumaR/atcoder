A, B, C = map(int, input().split())
mod_list = []
def_mod = A%B

for i in range(1,100):
    mod = (def_mod * i) % B
    if mod in mod_list:
        break
    else:
        mod_list.append(mod)
if C in mod_list:
    print("YES")
else:
    print("NO")