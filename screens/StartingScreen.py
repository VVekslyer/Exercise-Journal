from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

class StartingScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def move_text_upwards(self, widget, *args):
        animate = Animation(y = 250, duration = 2)
        animate.start(widget)