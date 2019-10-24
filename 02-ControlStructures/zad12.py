print('Zmienne x oraz y zawierają wartości całkowiete wprowadzone z klawiatury ')

x = int(input('Wprowadź wartość x: '))

y = int(input('Wrpowadź wartość y: '))

if x < 0 and y < 0:
    print('Liczby są ujemne')
elif x < 0 and y > 0:
    print(f'Liczba {x} jest ujemna')
elif x > 0 and y < 0:
    print(f'Liczba {y} jest ujemna')
else:
    print('Zadna z liczb x oraz y nie jest ujemna')