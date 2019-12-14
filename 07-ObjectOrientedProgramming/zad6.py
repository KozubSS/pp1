class Student():
    
    uczelnia = 'UEK Kraków'
    
    def __init__(self, name, sname, nralbum, kierunek):
        self.name = name
        self.sname = sname
        self.nralbum = 100000
        self.kierunek = kierunek
        
    def set_albumnr(self):
        self.nralbum = new_nralbum
        self.new_nralbum += 1
        
    def __str__(self):
        return self.name, self.sname, self.new_nralbum, self.kierunek, uczelnia
        
        
nowystudent = Student('Szymon', 'Kozub', 100000, 'Informatyka Stosowana')
print(nowystudent)
        