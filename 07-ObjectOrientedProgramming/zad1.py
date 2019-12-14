class musictrack():
    
    def __init__(self, author, titletrack, album, year):
        self.author = author
        self.titletrack = titletrack
        self.album = album
        self.year = year
        
    def __str__(self):
       # return 'Wykonawca:'+ self.author + '\n'+'Utwór: '+ self.titletrack + '\n'+'Album: '+ self.album + '\n'+'Rok:' + self.year
        return 'Wykonawca: {}, \nUtwór: {} \nAlbum: {} \nRok: {}'.format(self.author, self.titletrack, self.album, self.year)
    
    
jedynka = musictrack('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', '2018')
print(jedynka)