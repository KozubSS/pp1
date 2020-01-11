try:
    netto = float(input('Podaj wartość netto: '))
    brutto = netto*1.23
    print(brutto)
    if netto == 0 :
        raise ValueError('Wartość netto nie może być zerem.')
    if netto < 0:
        raise ValueError('Wartość netto nie może być ujemna.')
except TypeError:
    print('Podaj liczbe')
    
    