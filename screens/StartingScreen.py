from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.animation import Animation

class StartingScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def move_text_upwards(self, widget, *args):
        animate = Animation(y = 250, duration = 2)
        animate.start(widget)
        


Builder.load_string('''
<StartingScreen>:
    BlackBackground:

    H3:
        text: "Welcome."
        x: dp(55)
        y: root.height - dp(160)
        color: (1,1,1,1)
        #on_touch_down: root.move_text_upwards(self)

    Paragraph:
        text: "track your exercise progress for accountability."
        color: (1,1,1,1)
        y: root.height - dp(220)
        x: dp(55)

    AppButton:
        text: "Sign Up"
        width: root.width * 0.8
        height: root.height * 0.06
        size_hint: None, None
        size_hint_max: (dp(100), dp(5))
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_release: app.go_to(self, 'signup-with-email')

    Text:
        text: "Or"
        color: (1, 1, 1, 1)
        halign: 'center'
        pos_hint: {'center_y': 0.23}

    AppIconButton:
        text: "      Log in with Google"
        icon: "google"
        width: root.width * 0.8
        height: root.height * 0.06
        size_hint_max: (dp(100), dp(5))
        pos_hint: {'center_x': 0.5, 'center_y': 0.16}
        on_release: app.go_to(self, 'loading-screen')

    AppTextButton:
        text: "Or Log in"
        color: (1,1,1,1)
        pos_hint: {'center_x': 0.5, 'center_y': 0.09}
        on_release: app.go_to(self, 'login-screen')

''')
