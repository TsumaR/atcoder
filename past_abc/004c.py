"""
５と６を介して行ったが，一気に　30で行うべきだった
"""

N = int(input())
cards = [1, 2, 3, 4, 5, 6]

mod = N % 5
count_division = N // 5
mod_div = count_division % 6

div_cards = cards[mod_div:] + cards[:mod_div]

if mod == 0:
    print("".join(map(str, div_cards)))
    exit()
else:
    ans = div_cards[1:mod+1] + [div_cards[0]] + div_cards[mod+1:]
    print("".join(map(str, ans)))