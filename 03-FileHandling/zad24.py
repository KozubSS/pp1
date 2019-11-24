import csv
tab = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl' ],['Piotr','Wyga','wygap@gop.pl']]
fieldnames = ['Imie', 'Nazwisko', 'Email']

with open ('pliktestowy.csv', 'w') as plikCSV:
    writer = csv.writer(plikCSV, delimiter=',')
    writer.writerow(fieldnames)
    for x in tab:
        writer.writerow(x)