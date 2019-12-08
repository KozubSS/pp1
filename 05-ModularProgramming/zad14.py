import statistics as stat
import csv

wiek = []

with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        wiek.append(row[2])
        
wiek = [int(x) for x in wiek]

srednia = stat.mean(wiek)
mediana = stat.median(wiek)
odchylenie = stat.stdev(wiek)

print('Średnia arytmetyczna: {}\nMediana: {}\nOdchylenie standardowe: {}'
      .format(srednia,mediana,odchylenie))