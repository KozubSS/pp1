ocena = ['niedostateczny', 'mierny', 'dostateczny', 'dobry', 'bardzo dobry', 'celujący']

o = int(input('Podaj ocenę: od 1 do 6 '))

if o > 0 or o <= 6:
    print(f'Ocena słownie: {ocena[o-1]}')
else:
    print('Błędna ocena')