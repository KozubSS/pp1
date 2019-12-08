def wspak(tekst):
    return tekst[::-1]

def spacje(tekst):
    new = ''
    for char in tekst:
        new += (char+' ')
    return new


def wielka(tekst):
    tekst1 = ''
    rozdzielony = tekst.split(' ')
    for word in rozdzielony:
        index = 0
        for char in word:
            if index == 0:
                char = char.upper()
            else:
                char = char.lower()
            tekst1 += char
            index += 1
        tekst1 += ' '
    return tekst1
    