wiek = 22
if wiek < 0 or wiek > 120:
    raise ValueError(f'Podany wiek {wiek} powinien być liczbą całkowitą i mniejszą od 120!')
print(f'Masz {wiek} lat')