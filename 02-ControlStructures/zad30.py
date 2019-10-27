for i in range(3):
    if input('podaj PIN: ') == '0805':
        print('Działa')
        break
    else:
        print('Nieprawidłowy PIN')
    if i == 3:
        print('Karta płatnicza zostaje zablokowana')
        