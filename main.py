from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
#https://kivymd.readthedocs.io/en/latest/components/button/index.html

import sys
sys.path.insert(0, '/widgets/')
from widgets.StartingScreen import StartingScreen
from widgets.SignUpWithEmail import SignUpWithEmail
from widgets.WhatAreYourGoals import WhatAreYourGoals
from widgets.WhatIsYourWeight import WhatIsYourWeight
from widgets.WhatIsYourHeight import WhatIsYourHeight
from widgets.SettingsScreen import SettingsScreen
from widgets.UserSettings import UserSettings
from User import User


Builder.load_file('widgets/main.kv')

# Login and sign up screen.
class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

# Screen after an account has been created.
class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.Types_Of_Workouts = ["Leg Day", "Press Day", "Pull Day", "Rest Day"]
        


# Initialize app.
class App(MDApp):
    Window.set_title('Exercise Journal')
    Window.size = (360, 740)
    current_user = User(
        name = 'Vitaliy', 
        email = 'vitaly540@gmail.com', 
        goals = ['Strength'], 
        level = 'Beginner', 
        weight = 65, 
        height = 180)
    user_name = current_user.name
    def build(self):
        # These next few lines initialize the screen manager.
        # Our app is basically a collection of screens.
        # The app can be structured as five separate screens:
        #
        #             Starting Screen
        #         (Email, Height, Weight)
        #                    |
        #                  Login
        #                    |
        #             ______App______
        #            /       |       \
        #          Home   Workouts  Stats
        #                    
        self.sm = ScreenManager()
        self.sm.add_widget(StartingScreen(name='start-screen'))
        self.sm.add_widget(SignUpWithEmail(name='signup-with-email'))
        self.sm.add_widget(WhatAreYourGoals(name='what-are-your-goals'))
        self.sm.add_widget(WhatIsYourWeight(name='what-is-your-weight'))
        self.sm.add_widget(WhatIsYourHeight(name='what-is-your-height'))
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        self.sm.add_widget(UserSettings(name = 'user-settings'))    
        self.sm.current = 'home'
        
        
        self.screen_names = [
            'start-screen', 'signup-with-email', 'what-are-your-goals', 'what-are-your-goals', 'what-is-your-weight', 'what-is-your-height', 'login', 'home', 'settings', 'user-settings'
        ]

        menu_names = [
            "Settings","Info and Feedback", "Log Out"
        ]

        self.nameBoxes = ["Today", "Tomorrow", "Day After"]
        self.TitleCounter = 0
        triple_dots_menu_items = [{
            "viewclass": "OneLineListItem",
            "text": f"{i}",
            "height": dp(56),
            "on_release": lambda x=f"{i}": self.vertical_menu_item_pressed(x),
        } for i in menu_names]

        self.menu = MDDropdownMenu(
            items=triple_dots_menu_items,
            width_mult=4,
        )

        prev = self.sm.current
        for screen in self.screen_names:
            self.sm.current = screen
        self.sm.current = prev

        return self.sm

    # Menu functions
    def callback(self, button):
        self.menu.caller = button
        self.menu.open()

    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def vertical_menu_item_pressed(self, text_item):
        self.menu.dismiss()

        if text_item == "Settings":
            self.sm.transition.direction = 'left'
            self.sm.current = 'settings'
        elif text_item == "User Settings":
            pass
        elif text_item == "Info and Feedback":
            pass
        elif text_item == "Log Out":
            self.show_logout_dialog()

    # Transitions
    def go_to(self, button, screen):
        self.sm.transition.direction = 'left'
        self.sm.current = screen

    def go_back(self, button, screen):
        self.sm.transition.direction = 'right'
        self.sm.current = screen

    def show_logout_dialog(self, *args):
        self.dialog = MDDialog(
            text="Log out?",
            buttons=[
                MDFlatButton(
                    text="YES",
                    theme_text_color="Custom",
                    text_color=(1, 0, 0, 1),
                ),
                MDFlatButton(
                    text="NO",
                    theme_text_color="Custom",
                    text_color=(1, 0, 0, 1),
                    on_release = self.dismiss_dialog,
                ),
            ],
            radius=[20, 20, 20, 20],
        )
        self.dialog.open()
    
    def dismiss_dialog(self, *args):
        self.dialog.dismiss(force=True)
        self.sm.current = 'home'


if __name__ == '__main__':
    App().run()
