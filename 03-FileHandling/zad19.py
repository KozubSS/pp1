tablica = []

with open ('universities.txt', 'r') as plik:
    for line in plik:
        tablica.append(line)
        
tablica.sort()

with open ('universities.txt', 'w') as plik:
    for x in tablica:
        plik.write(x)