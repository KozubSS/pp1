import re

sgloski = ['a', 'e', 'i', 'o', 'u', 'y']

w = '''Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na
pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się
szeregi, Prosto, długo, daleko, jako morza brzegi.'''

for x in sgloski:
    print(f'''{x}: {len(re.findall(x, w))}''')