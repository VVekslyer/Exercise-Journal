from kivy.uix.screenmanager import Screen

class SignUpWithEmail(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def build(self):
        return SignUpWithEmail()