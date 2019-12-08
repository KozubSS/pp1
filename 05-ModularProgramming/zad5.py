import statistics as stat


tablica= [21600, 4350, 3920, 5590, 3250, 4010]

print(f'Średnia arytmetyczna: {stat.mean(tablica)}')
print(f'Mediana: {stat.median(tablica)}')
print(f'Odchylenie standardowe: {stat.stdev(tablica)}')
