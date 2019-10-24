
tablica = [15,8,31,47,2,19]
i = 0
p = 0
for x in tablica:
    if x % 2 != 0:
        p += x
        i += 1
    av = p/i
print(f'Średnia arytmetyczna liczb nieparzystych wynosi: {av}')


