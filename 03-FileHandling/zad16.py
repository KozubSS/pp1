import re

komunikat = 'wtorek - 23Cm środa - 17C, czwartek - 25C'
cyfry = re.findall('\d{2}', komunikat)


print(sum([int(x) for x in cyfry]) / len(cyfry))


