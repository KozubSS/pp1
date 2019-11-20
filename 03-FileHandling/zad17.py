import re

tekst = 'To be, or not to be, that is the question'

samogloski = re.findall('[aeiouy]', tekst)
print(len(samogloski))