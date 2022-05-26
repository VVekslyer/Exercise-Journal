from kivy.uix.widget import Widget

class CalendarDay(Widget):

    def toggle(self, icon_button):
        self.ids.date_button.icon = 'assets/images/calendar-circle.png'