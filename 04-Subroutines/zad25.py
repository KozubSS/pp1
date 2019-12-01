def jestImie(imie, imiona):
    if imie in imiona:
        return 'Imię zawarte jest w wykazie imion'
    else:
        return 'Imię nie znajduje się w wykazie imion'

name = 'Wojtek'
names = ['Janek', 'Ania', 'Wojtek', 'Zosia']

print('Imiona: {}\nImię: {}\nRezultat: {}'.format(
    ' '.join(names), name, jestImie(name, names)))