from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class LoadingScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

Builder.load_string('''
<LoadingScreen>:
    MDFloatLayout:
        H4:
            text: 'Loading...'
            halign: 'center'
            valign: 'middle'
            font_size: '30sp'
        ''')

