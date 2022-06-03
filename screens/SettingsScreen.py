from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors


class SettingsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.orientation = 'vertical'
    
    def build(self):
        return SettingsScreen()
    
    
    
        
        
        
        
         
