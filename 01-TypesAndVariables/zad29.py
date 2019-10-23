from random import randint

x = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))
k = randint(1,6)
print(f'Komputer wyrzucił: {k}')
if x == k:
    print('Zgadłeś: True')
else:
    print('Zgadłeś: False')
