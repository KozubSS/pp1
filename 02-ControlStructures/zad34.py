np = input('Wprowadź numer PESEL: ')
int(np)
year = np[0] + np[1]
month = np[2] + np[3]

if int(month) in range(1, 13):
    year = '19' + year
elif int(month) in range(21, 33):
    year = '20' + year
elif int(month) in range(81, 93):
    year = '18' + year

wiek = 2018 - int(year)


if int(np[-2]) % 2 == 0:
    gender = 'Kobieta'
else:
    gender = 'Mężczyzna'

print(f'Płeć: ', gender)
print(f'Wiek: ', wiek)