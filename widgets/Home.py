from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.clock import Clock

class Home(MDBottomNavigationItem):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.current_chosen_date = None
        Clock.schedule_once(self.set_default_date)

    def set_default_date(self, *args):
        self.current_chosen_date = self.ids.i_0

        

class Content(MDBoxLayout):
    pass

class ExercisesList(MDBoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.workouts = ["Push Day", "Pull Day", "Leg Day", "Cardio Day"]
        Clock.schedule_once(self.generate_panel)


    # TODO Change the font and font size using Kivy markup
    # * https://kivy.org/doc/stable/api-kivy.core.text.markup.html
    
    def generate_panel(self, *args):
        for i in range(4):
            self.ids.box.add_widget(MDExpansionPanel(
                panel_cls = MDExpansionPanelOneLine(
                    text = f'    [size=20sp][font=assets/fonts/Sofia-Pro-Semi-Bold.ttf]{self.workouts[i]}[/font][/size]'
                ),
                content = Content()
            )
        )

        
