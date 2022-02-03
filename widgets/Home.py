from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from kivymd.uix.bottomnavigation import MDBottomNavigationItem

class Home(MDBottomNavigationItem):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.workouts = ["Leg Day", "Press Day", "Pull Day", "Rest Day"]