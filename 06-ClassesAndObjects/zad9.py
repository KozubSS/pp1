class University():
    
    def __init__(self):
        self.name = 'UEK'
        self.fullname = ''
        
    def print_name(self):
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name
        
    def set_fullname(self, fullname):
        self.fullname = fullname
        
    def print_fullname(self):
        print(self.fullname)
        
moja_klasa = University()
moja_klasa.set_name('AGH')
moja_klasa.print_name()
moja_klasa.print_fullname()
moja_klasa.set_fullname('Uniwersyalksfhasdjfh')
moja_klasa.print_fullname()

