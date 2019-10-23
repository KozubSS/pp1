a = int(input("Wartość boku a "))
b = int(input("Wartość boku b "))
c = int(input("Wartość boku c "))

z = (((a + b + c)  *(a + b - c) * (a - b + c) * (-a + b + c)) ** (1/2)) /4
print(f'Pole wynosi: {z}')