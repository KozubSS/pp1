x = int(input('Podaj kwote: '))

a5 = x // 5
a2 = (x - a5 * 5) // 2
a1 = x - a5 * 5 - a2 * 2
print(f'5 zł: {a5} szt.')
print(f'2 zł: {a2} szt.')
print(f'1 zł: {a1} szt.')