par = 0

npar = 0

for x in range(1,51):
    if x % 2 == 0:
        par += x
    else:
        npar += x
        
print(f'Suma liczb parzystch {par}\nSuma liczb nieparzystych {npar}\nZ przedziału <1,50>')