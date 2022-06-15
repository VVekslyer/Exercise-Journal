from kivymd.uix.button import MDFloatingActionButtonSpeedDial

class FloatingPlusButton(MDFloatingActionButtonSpeedDial):
    def __init__(self, **kwargs):
        super(FloatingPlusButton, self).__init__(**kwargs)

        options = {
            'Recommendations' : 'star',
            'Create workout' : 'lightning-bolt'
        }

        self.rotation_root_button = True
        self.data = options
        self.bg_color_root_button =  (0,0,0,1)
        self.bg_color_stack_button = (0,0,0,1)
        self.text_color = (1,1,1,1)