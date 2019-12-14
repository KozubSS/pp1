class TV():
    
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    
    def off(self):
        self.is_on = False
    
    def on(self):
        self.is_on = True
    
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        if self.is_on:
            self.channels = channels_list
            
        else:
            print('Nie można zaprogramować programów przy wyłączonym telewizorze')
        
    def show_channels(self):
        print(self.channels)
        
    def show_status(self):
        if self.is_on and self.channels != []:
            print('Telewizor jest załączony, kanał {}, {}.'.format(self.channel_no, self.channels[self.channel_no - 1]))
        elif self.is_on == True:
            print('Telewizor jest załączony, kanał {}.'.format(self.channel_no))
        else:
            print('Telewizor nie jest załączony')
            
    
            
telew = TV()
telew.show_status()
telew.on()
telew.show_status()
telew.show_channels()
telew.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'TTV', 'Jetix'])
telew.show_channels()
telew.set_channel(5)
telew.show_status()
telew.off()


