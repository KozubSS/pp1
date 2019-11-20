tab = [32, 16, 5, 8, 24, 7]

with open('zad13tablica.txt', 'w') as plik:
    plik.write('\n '.join([str(x) for x in tab]))