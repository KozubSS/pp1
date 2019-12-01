

def podatek(dochod):
    if dochod < 0:
        return False
    elif dochod <= 5000:
        return dochod*0.17
    else:
        return 5000*0.17+(dochod-5000)*0.32
    
p = int(input('Podaj dochód: '))
assert p > 0
print(f'Podatek należny: {podatek(p)} zł')