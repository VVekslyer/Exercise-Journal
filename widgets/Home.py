from kivymd.uix.bottomnavigation import MDBottomNavigationItem

class Home(MDBottomNavigationItem):
    def __init__(self, **kw):
        super().__init__(**kw)
    
        self.name = 'screen 1'
        self.text = 'Home'
        self.icon = 'home'