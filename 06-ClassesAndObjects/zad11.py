class TV():
    
    def __init__(self):
        self.is_on = 'off'
        self.channel_no = 1
    
    def off(self):
        self.is_on = 'off'
    
    def on(self):
        self.is_on = 'on'
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def show_status(self):
        if self.is_on == 'on':
            print('Telewizor jest załączony, kanał {}.'.format(self.channel_no))
            
        else:
            print('Telewizor nie jest załączony')
            
    
            
telew = TV()
telew.show_status()
telew.on()
telew.show_status()
telew.set_channel(5)
telew.show_status()
telew.off()
telew.show_status()