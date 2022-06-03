from kivy.uix.screenmanager import Screen

class WhatIsYourHeight(Screen):
    def __init__(self, **kw):
        unit = "FT"
        super().__init__(**kw)

    def toggle(self, text_button):
        unit = text_button.text.replace(" ", "")
        text_button.font_name = 'assets/fonts/Sofia-Pro-Semi-Bold.ttf'
        
        if unit == 'CM':
            self.ids.ft.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        elif unit == 'FT':
            self.ids.cm.font_name = 'assets/fonts/Sofia-Pro-Light.ttf'
        