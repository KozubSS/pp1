numery = []

with open ('numbersinrows.txt', 'r') as file:
    for line in file:
        for number in line.split(','):
            numery.append(int(number))

print(f'Ilość liczb: {len(numery)}\nSuma: {sum(numery)}')
