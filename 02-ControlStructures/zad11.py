login = ('marek')
haslo = ('m-123')

print('Logowanie do systemu')

login_acc = input('Podaj login: ')

haslo_acc = input('Podaj hasło: ')

if login_acc == login and haslo_acc == haslo:
    print('Podane dane są prawidłowe')
else:
    print('Podane dane są nieprawidłowe')