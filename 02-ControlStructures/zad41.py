x = []
while True:
    a = int(input('Podaj liczbe: '))
    
    if a == 0:
        print(f'REZULTAT: Liczb={len(x)}, Suma={sum(x)}, Średnia={sum(x) / len(x)}')
        break
    x.append(a)