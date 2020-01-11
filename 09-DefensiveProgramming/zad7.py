def wskaznik_bmi():

    waga = float(input('Wprowadź swoją wage: '))
    assert type(waga) == float, 'Błędna wartość'
    assert waga in range(40,151), 'Waga nie mieści sie w przedziale <40;150>'
    wzrost = int(input('Podaj wzrost w cm" '))
    assert type(wzrost) == int  , 'Błędna wartość'
    assert wzrost in range(150,221), 'Wzrost nie mieści się w przediale <150,220>'
    
    waga = float(waga)
    wzrost = int(wzrost)
    bmi = waga/(wzrost/100)**2
    print(bmi)
    

wskaznik_bmi()
    
    

