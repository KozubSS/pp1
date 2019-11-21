tablica = []

with open ('numbers.txt', 'r') as plik:
    for line in plik:
        if int(line) % 2 == 0:
            tablica.append(line)
            
with open ('evennumbers.txt', 'w') as file:
    for x in tablica:
        file.write(str(x) + '\n')
        tablica.sort()
        
        