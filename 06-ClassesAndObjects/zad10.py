class TV():
    
    def __init__(self):
        self.is_on = 'off'
        self.channel_no = 1
    
    def off(self):
        self.is_on = 'off'
    
    def on(self):
        self.is_on = 'on'
        
       
        
    def show_status(self):
        if self.is_on == 'on':
            print('Telewizor jest załączony, kanał {}.'.format(self.channel_no))
            
        else:
            print('Telewizor nie jest załączony')
            
    
            
telew = TV()
telew.on()
telew.show_status()
telew.off()
telew.show_status()