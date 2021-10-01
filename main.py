# Make sure pip installer is updated to latest version in order to run.
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('main.kv')

# Declare both screens
class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SettingsScreen(Screen):
    pass

class App(MDApp):
    Window.size = (410, 730)

    options = {
            'Recommendations' : 'star',
            'Create workout' : 'lightning-bolt'
        }
    
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    App().run()