tab = []

with open ('numbers.txt', 'r') as file:
    for x in file:
        tab.append(int(x))
        
tab.sort()
for y in tab:
    print(y, end = ' ')