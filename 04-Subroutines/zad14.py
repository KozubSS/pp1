
tab = [15, 38, 7, 23, 14]
liczba = 23
def wystepuje(liczba,tab):
    if liczba in tab:
        print(f'Liczba: {liczba}')
        print(f'Tablica: {tab}')
        print('Rezultat: Podana liczba wysępuje w tab')
    else:
        print(f'Liczba: {liczba}')
        print('Rezultat: Podana liczba nie wysępuje w tab')
        
wystepuje(liczba,tab)
        
        
