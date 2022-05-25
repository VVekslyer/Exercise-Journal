from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelLabel, MDExpansionPanelOneLine
from kivymd import images_path
from kivy.clock import Clock

class Home(MDBottomNavigationItem):
    def __init__(self, **kw):
        super().__init__(**kw)

class Content(MDBoxLayout):
    pass

class ExercisesList(MDBoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.workouts = ["Push Day", "Pull Day", "Leg Day", "Cardio Day"]
        Clock.schedule_once(self.generate_panel)

    def generate_panel(self, *args):
        for i in range(3):
            self.ids.box.add_widget(MDExpansionPanel(
                panel_cls = MDExpansionPanelOneLine(
                    text = f'    {self.workouts[i]}'
                ),
                content = Content()
            )
        )

        
