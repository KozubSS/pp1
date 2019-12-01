from random import randint


def rzucKostka():
    x = 3
    suma=[]
    if x==0:
        print('Brak rzutu równa się zakończeniem gry')
    else:
        for y in range(x):
            suma.append(randint(1,11))
    print ('Wyrzucone oczka: {0}'.format(' '.join(map(str, suma))))
    print ('Suma oczek wynosi: {0}'.format(sum(suma)))
    
rzucKostka()