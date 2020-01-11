import math
while True and number >0:
    try:
        number = float(input('Enter any number: '))
        print (f'sqrt({number}) = {math.sqrt(number)}' )

    except:
        print('Please enter a valid number greater than 0')
