def pole_prostokata():
        a = int(input('Podaj wartośc boku a: '))
        b = int(input('Podaj wartośc boku b: '))
        pole = a*b
        assert a > 0 and b > 0, 'Wartości boków są ujemne'
        
        return print(pole)

               
pole_prostokata()


