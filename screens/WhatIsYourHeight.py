from kivy.uix.screenmanager import Screen

class WhatIsYourHeight(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.unit = 'FT'

    def toggle(self, text_button):
        self.unit = text_button.text.replace(" ", "")
        text_button.font_name = 'assets/fonts/Sofia-Pro-Semi-Bold.ttf'
        
        if self.unit == 'CM':
            self.ids.ft.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        elif self.unit == 'FT':
            self.ids.cm.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        