from kivy.uix.screenmanager import Screen

class WhatIsYourWeight(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.unit = 'LBS'
    
    def toggle(self, text_button):
        self.unit = text_button.text.replace(" ", "")
        text_button.font_name = 'assets/fonts/Sofia-Pro-Semi-Bold.ttf'
        
        if self.unit == 'KG':
            self.ids.lbs.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        elif self.unit == 'LBS':
            self.ids.kg.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        