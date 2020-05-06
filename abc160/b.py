X = int(input())

fi_hun = X // 500
fi_mod = X % 500

fi = fi_mod // 5

print(fi_hun * 1000 + fi * 5)