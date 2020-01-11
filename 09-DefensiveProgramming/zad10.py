try:
    with open('NoEducation.txt', newline='') as file:
        print(file.read())
except:
    print('Brak pliku o takiej nazwie')
        