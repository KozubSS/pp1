from random import randint



rzut = [randint(1,6) for x in range(100)]
print(f'Jedynka: {rzut.count(1)}')
print(f'Dwójka: {rzut.count(2)}')
print(f'Trójka: {rzut.count(3)}')
print(f'Czwórka: {rzut.count(4)}')
print(f'Piątka: {rzut.count(5)}')
print(f'Szóstka: {rzut.count(6)}')
     