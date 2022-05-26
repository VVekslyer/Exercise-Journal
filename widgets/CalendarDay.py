from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget

class Date(MDIconButton):
    def toggle(self, icon_button, *args):
        icon_button.icon = 'assets/images/calendar-circle.png'

class DateLabel(MDLabel):
    def toggle(self, label, *args):
        label.color = (0,0,0,1)

class CalendarDay(Widget):
    def toggle(self, icon_button, *args):
        self.ids.date_button.icon = 'assets/images/calendar-circle.png'