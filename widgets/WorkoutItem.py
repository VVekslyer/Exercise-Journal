from kivymd.uix.card import MDCard

class WorkoutItem(MDCard):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.orientation = 'vertical'
        self.padding = '8dp'
        self.size_hint = (None, None)
        self.size = ('280dp', '180dp')
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.backdrop = 30
        self.md_bg_color = (0.23,0.25,0.30,1)
        self.border = (90,90,90,90)