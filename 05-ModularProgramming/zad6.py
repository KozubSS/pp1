       

import csv
from statistics import mean

tryb = input('A czy B? ')

if tryb == 'a' or tryb == 'A':
    with open('employees.csv', newline='') as f:
        reader = csv.reader(f)
        z = 0
        for row in reader:
            if z == 0:
                print('{:<5}{:<15}{:<15}{:<6}{:<34}'.format(
                    '#', row[0].upper(), row[1].upper(), row[2].upper(), row[3].upper()))
                linie = '='*75
                print(linie)
            else:
                print('{:<5}{:<15}{:<15}{:<6}{:<25}'.format(
                    z, row[0], row[1], row[2], row[3]))
            z += 1
else:
    with open('employees.csv', newline='') as f:
        reader = csv.reader(f)
        z, ages = 0, []
        for row in reader:
            if z != 0:
                ages.append(row[2])
            z += 1
        ages = [int(x) for x in ages]
        print(mean(ages))