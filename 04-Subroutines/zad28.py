def rysujWykres(jezyki, wartosci):
    for x, y in zip(jezyki, wartosci):
        print(f'''{x:10}: {'#' * (y // 3)}''')


jezyki = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

rysujWykres(jezyki, wartosci)