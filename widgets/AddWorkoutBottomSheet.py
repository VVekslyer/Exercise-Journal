from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

class AddWorkoutBottomSheet(BoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

class Tab(MDFloatLayout, MDTabsBase):
    # Tab content
    content_text = StringProperty('')

Builder.load_string('''
<AddWorkoutBottomSheet>:
    orientation: "vertical"
    size_hint_y: None
    height: "400dp"

    MDToolbar:
        title: '[color=#000000][font=assets/fonts/Sofia-Pro-Semi-Bold.ttf]Add Workout[/font][/color]'
        md_bg_color: (1,1,1,1)
    
    MDBoxLayout:
        orientation: 'vertical'
        MDTextField:
            id: field
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: None
            width: "200dp"
            hint_text: "Workout Type"
            #on_focus: if self.focus: app.menu.open()

    
''')
