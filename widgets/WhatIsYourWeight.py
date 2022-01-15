from kivy.uix.screenmanager import Screen

class WhatIsYourWeight(Screen):
    def __init__(self, **kw):
        unit = "LBS"
        super().__init__(**kw)
    
    def toggle(self, text_button):
        unit = text_button.text.replace(" ", "")
        text_button.font_name = 'assets/fonts/Sofia-Pro-Semi-Bold.ttf'
        
        if unit == 'KG':
            self.ids.lbs.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        elif unit == 'LBS':
            self.ids.kg.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        