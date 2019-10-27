a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

delta = b ** 2 - 4 * a * c
if delta > 0:
    x1 = (-b + delta **(1/2)) / 2*a
    x2 = (-b - delta **(1/2)) / 2*a
    print(f'Miejsca zerowe: \nx1: {x1}\nx2: {x2}')
elif delta == 0:
    x0 = -b / (2 * a)
    print(f'x0: {x0}')
else:
    print('Brak rozwiązań')