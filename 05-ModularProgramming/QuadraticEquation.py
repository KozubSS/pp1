
def czytajWspolczynnik():
    a = int(input('Podaj współczynnik a: '))
    b = int(input('Podaj współczynnik b: '))
    c = int(input('Podaj współczynnik c: '))
    print('Równanie kwadratowe postaci: {}x2{}{}x{}{}=0'.format( a, "" if b < 0 else "+", b, "" if c < 0 else "+", c))
    return [a, b, c]
    

def obliczDelte(entry):
    a = int(entry[0])
    b = int(entry[1])
    c = int(entry[2])
    delta = b**2 - 4*a * c
    return delta


def obliczPierwiastki(entry):
    a = int(entry[0])
    b = int(entry[1])
    c = int(entry[2])
    delta = obliczDelte(entry)
    if delta > 0:
        sqrt_delta = delta ** (1/2)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return [x1, x2]
    elif delta == 0:
        x0 = -b / (2*a)
        return [x0]
    else:
        return []


def wyswietlPierwiastki(list_x1_x2_x0):
    if len(list_x1_x2_x0) == 2:
        print(f'Pierwiastki równania: x1 = {list_x1_x2_x0[0]}, x2 = {list_x1_x2_x0[1]}')
    elif len(list_x1_x2_x0) == 1:
        print(f'Pierwiastek równania: x = {list_x1_x2_x0[0]}')
    else:
        print('Brak rozwiązań równania')