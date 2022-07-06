from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget

class CalendarDay(Widget):
    def toggle(self, icon_button, *args):
        icon_button.icon = 'assets/images/calendar-circle.png'

class Date(MDIconButton):
    def toggle(self, date_label, *args):
        self.icon = 'assets/images/calendar-circle.png'
        date_label.color = (1,1,1,1)
    

class DateLabel(MDLabel):
    def toggle(self, label, *args):
        label.color = (0,0,0,1)


