import re
tab = []

with open ('land.txt', 'r') as file:
    for x in file:
        x = re.findall('\d', file.read())
        x = [int(k) for k in x]
        
    print(f'Suma cyfr w pliku land.txt: {sum(x)}')