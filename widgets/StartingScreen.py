from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

class StartingScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def animate_text(self, widget, *args):
        animate = Animation(
        pos_hint = { "center_y" : 0.1}
        )
        print("animate!")
        animate += Animation(y = 250, duration = 2)
        animate.start(widget)