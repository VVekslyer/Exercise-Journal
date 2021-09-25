# Make sure pip installer is updated to latest version in order to run.

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Window.size = (410, 730)


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'vitaly540@gmail.com'
            right_action_items: [["dots-vertical"]]
            md_bg_color: app.theme_cls.bg_light
            left_action_items: [["menu"]]
            specific_text_color: (0, 0, 0, 1)
            elevation: 5
        Button:
            text: 'Progress'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        # App Theme
        

        return sm

if __name__ == '__main__':
    TestApp().run()