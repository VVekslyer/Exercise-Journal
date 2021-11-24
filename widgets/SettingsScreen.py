from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class SettingsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.orientation = 'vertical'
    
    def build(self):
        return SettingsScreen()
    
    
    
        
        
        
        
         
