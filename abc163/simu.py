while True:   
    n = int(input('正の数を入力してください: '))
    if n <= 0:
        print('n <= 0')
    else:
        for i in range(n+1):
            print(i)