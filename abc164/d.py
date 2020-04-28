"""
各Tiのmodを計算する。
共通のmodがいくつあるかを調べる。
"""

s = input()[::-1]

# 0が2019個からなるリスト。modを保管する
cnts = [0] * 2019
cnts[0] = 1
mod_num = 0
d = 1

for c in s:
  t = d * int(c)
  mod_num += t
  mod_num %= 2019
  cnts[mod_num] += 1
  d *= 10
  d %= 2019

result = 0
for cnt in cnts:
  result += cnt * (cnt - 1) // 2

print(result)


# ans = 0
# for cnt in cnts:
#   ans += cnt * (cnt - 1) // 2
