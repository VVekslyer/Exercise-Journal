from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from widgets.AddWorkoutBottomSheet import AddWorkoutBottomSheet
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.toast import toast
from kivy.clock import Clock

class Home(MDBottomNavigationItem):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.current_chosen_date = None
        Clock.schedule_once(self.set_default_date)

    def set_default_date(self, *args):
        self.current_chosen_date = self.ids.day1
    
    def set_new_chosen_date(self, *args):
        pass

    def callback_for_menu_items(self, *args):
        toast(args[0])

    def open_add_exercise_bottom_sheet(self):
        bottom_sheet_menu = MDCustomBottomSheet(screen=AddWorkoutBottomSheet())
        bottom_sheet_menu.open()


class Content(MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

class ExercisesList(MDBoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.workouts = ["Push Day", "Pull Day", "Leg Day", "Cardio Day"]
        Clock.schedule_once(self.generate_panel)
    
    def generate_panel(self, *args):
        for i in range(4):
            self.ids.box.add_widget(MDExpansionPanel(
                panel_cls = MDExpansionPanelOneLine(
                    text = f'    [size=20sp][font=assets/fonts/Sofia-Pro-Semi-Bold.ttf]{self.workouts[i]}[/font][/size]'
                ),
                content = Content()
            )
        )

        
