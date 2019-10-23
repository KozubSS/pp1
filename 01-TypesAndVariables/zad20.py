'''
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
'''
import math

# ustal promień koła i Pi
r = 5
pi = math.pi

# oblicz pole i obwód
poleK = pi * r**2
obwK = 2 * pi * r

#wyświetl rezultaty
print(f'Pole koła o promieniu {r} wynosi {poleK}')
print(f'Obwód koła o promieniu {r} wynosi {obwK}')
