from GBP import GBP

print('Data\t\t Kurs')
print('----------------------------')

for k in GBP['rates']:
    print(f'k['effectiveDate']:10,'\t',k['mid'])
    
    
    
    