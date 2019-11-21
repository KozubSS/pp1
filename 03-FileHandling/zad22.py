import csv


with open ('students.txt', 'r') as file:
    csvreader = csv.DictReader(file)
    for x in csvreader:
        if int(x['age']) < 30:
            print(f"{x['first_name']:9}{x['last_name']:9}{x['email']:10}")
            
            #w pliku txt po emails musiałem dodać ,
            
        