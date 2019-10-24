x = int(input('zmienna x: '))
y = int(input('zmienna y: '))

for i in range(1, x + 1):
    if i == 1 or i == x:
        print('*' * y)
    else:
        print('*' + ' ' * (y-2) + '*')