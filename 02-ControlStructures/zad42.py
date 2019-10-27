x = int(input('Podaj liczbe: '))
z = int(input('Podaj liczbe: '))

try:
    print(f'Wynik: {x/z}')
except ZeroDivisionError:
    print('Dzielenie przez 0')