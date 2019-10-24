# zadanie 13

x = float(input('Pierwsza współrzędna: '))
y = float(input('Druga współrzędna: '))

if x > 0 and y > 0:
    print(x)
    print(y)
    print(f'Punkt P({x},{y}) znajduję sie w pierwszej ćwiartce układu współrzędnych')
elif x < 0 and y > 0:
    print(x)
    print(y)
    print(f'Punkt P({x},{y}) znajduje się w drugiej ćwiartce układu współrzędnych')
elif x < 0 and y < 0:
    print(x)
    print(y)
    print(f'Punkt P({x},{y}) znajduje się w trzeciej ćwiartce układu współrzędnych')
elif x == 0 and y == 0:
    print(x)
    print(y)
    print(f'Punkt P({x},{y}) znajduje się w punkcie przecięcia się układu współrzędnych')
else:
    print(x)
    print(y)
    print(f' Punkt P({x},{y}) znajduje się w czwartej ćwiartce układu współrzędnych')


    
    
    