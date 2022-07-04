from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from screens.StartingScreen import StartingScreen
from screens.LoginScreen import LoginScreen
from screens.SignUpWithEmail import SignUpWithEmail
from screens.WhatAreYourGoals import WhatAreYourGoals
from screens.WhatIsYourLevel import WhatIsYourLevel
from screens.WhatIsYourWeight import WhatIsYourWeight
from screens.WhatIsYourHeight import WhatIsYourHeight
from screens.WhatIsYourName import WhatIsYourName
from screens.SettingsScreen import SettingsScreen
from screens.UserSettings import UserSettings
from screens.AddWorkout import AddWorkoutScreen
from screens.LoadingScreen import LoadingScreen
from sources.User import User

# This import is used to establish DNS server connections with Android and iOS devices.
import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception
from pymongo import MongoClient, errors
import motor.motor_asyncio
import asyncio
import datetime

# use a try-except indentation to catch MongoClient() errors
try:
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://PaulColonia:blabla33@journaldb.qf9cz.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

    db = client.UserInfo
    colection = db.test_collection
    people = db.people

except errors.ServerSelectionTimeoutError as err:
    # set the client and DB name list to 'None' and `[]` if exception
    print("ERROR")
    print(err)

# Screen after an account has been created.
class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

# Initialize app.
class App(MDApp):
    Window.title = 'Exercise Journal'
    #Window.size = (360, 740)
    current_user = User(
        name = '',
        gender = '', 
        email = '', 
        goals = '', 
        level = '', 
        weight = 0,
        height = 0)
    user_is_making_new_account = True
    
    def build(self):
        self.title = 'Exercise Journal'
        # These next few lines initialize the screen manager.
        # Our app is a collection of screens.
        # The app can be structured as five separate screens:
        #
        #             Starting Screen
        #      (Email, Height, Weight, Name)
        #                    |
        #                  Login
        #                    |
        #             ______App______
        #            /       |       \
        #          Home   Workouts  Stats
        #                    
        self.sm = ScreenManager()
        self.sm.add_widget(StartingScreen(name='start-screen'))
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(LoginScreen(name='login-screen'))
        self.sm.add_widget(SignUpWithEmail(name='signup-with-email'))
        self.sm.add_widget(WhatAreYourGoals(name='what-are-your-goals'))
        self.sm.add_widget(WhatIsYourLevel(name='what-is-your-level'))
        self.sm.add_widget(WhatIsYourWeight(name='what-is-your-weight'))
        self.sm.add_widget(WhatIsYourHeight(name='what-is-your-height'))
        self.sm.add_widget(WhatIsYourName(name='what-is-your-name'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        self.sm.add_widget(UserSettings(name='user-settings'))
        self.sm.add_widget(AddWorkoutScreen(name='add-workout'))
        self.sm.add_widget(LoadingScreen(name='loading-screen'))
        self.sm.current = 'home'

        menu_names = [
            "Settings", "Info","Tutorial", "Log Out"
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

        if text_item == 'Settings':
            self.sm.transition.direction = 'left'
            self.sm.current = 'settings'
        elif text_item == 'User Settings':
            pass
        elif text_item == 'Info and Feedback':
            pass
        elif text_item == 'Log Out':
            self.show_logout_dialog()

    # Transitions
    def go_to(self, button, screen):
        self.sm.transition.direction = 'left'
        self.sm.current = screen

    def go_back(self, button, screen):
        self.sm.transition.direction = 'right'
        self.sm.current = screen
    
    def log_out(self, *args):
        self.sm.transition.direction = 'right'
        self.sm.current = 'start-screen'

    def show_logout_dialog(self, *args):
        self.dialog = MDDialog(
            text="Log out?",
            buttons=[
                MDFlatButton(
                    text="YES",
                    theme_text_color="Custom",
                    text_color=(0.73, 0.49, 0.28, 1),
                    on_release = self.log_out,
                    on_press = self.dismiss_dialog
                ),
                MDFlatButton(
                    text="NO",
                    theme_text_color="Custom",
                    text_color=(0.73, 0.49, 0.28, 1),
                    on_release = self.dismiss_dialog,
                ),
            ],
            radius=[20, 20, 20, 20],
        )
        self.dialog.open()
    
    def dismiss_dialog(self, *args):
        self.dialog.dismiss(force=True)
        self.sm.current = 'home'

    def clientLoop(self):
        loop = client.get_io_loop()
        loop.run_until_complete(self.db_insert_new_user())
      
    async def db_insert_new_user(self):
        if self.user_is_making_new_account:
            userDocument = {
              "name" : self.current_user.name,
              "gender" : None,
              "email" : self.current_user.email,
              "goals" : self.current_user.goals, 
              "level" : self.current_user.level, 
              "weight" : self.current_user.weight,
              "height" : self.current_user.height
            }
            if await db.test_collection.find_one({"name": userDocument["name"]}):
                print("Same user was found.")
            else:
                await db.test_collection.insert_one(userDocument)
                print(self.current_user.name, 'inserted into the database!')
                self.user_is_making_new_account = False
                

Builder.load_file('main.kv')

if __name__ == '__main__':
    App().run()
