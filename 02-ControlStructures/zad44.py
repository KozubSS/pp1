x = int(input('Podaj limit prędkości (km/h): '))
v = int(input('Podaj prędkość pojazdu (km/h): '))
przekroczenie = v - x

if przekroczenie > 10:
    print(f'Mandat: {50 + ((przekroczenie - 10) * 15)} zł')
elif przekroczenie < 10 and przekroczenie > 0:
    print(f'Mandat: {przekroczenie * 5} zł')
elif przekroczenie <= 0:
    print('Brak mandatu')
    