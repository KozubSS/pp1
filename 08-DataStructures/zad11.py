from GBP import GBP

print(f'Data\t\tKurs')
print('----------------------------')

for k in GBP['rates']:
    print(k['effectiveDate'],'\t   ',k['mid'])
    
    
    
    