from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from datetime import date

class Home(MDBottomNavigationItem):
    def __init__(self, **kw):
        super().__init__(**kw)
    
        self.name = 'screen 1'
        self.text = 'Home'
        self.icon = 'home'

    # date() function is still incomplete.
    # If a workout's date is today, the header of the workout item will be "Today"
    # If a workout's date it tomorrow, the header of the workout item will be "Tomorrow"
    # Otherwise, it will just display the day of the week ("Monday", "Tuesday", "Wednesday" ...)
    def date():
        today = date.today()
        return date(2021, 12, 20)