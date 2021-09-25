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
            left_action_items: [["account-circle"]]
            right_action_items: [["dots-vertical"]]
            md_bg_color: app.theme_cls.bg_light
            specific_text_color: (0,0,0,1)
            elevation: 0
        MDLabel:
            text: 'Home'
            halign: 'left'
            padding_x: '12dp'
            padding_y: '12dp'
            adaptive_size: True 
            text_color: (0,0,0,1)
            font_style: 'H4'
        Button:
            text: 'Workout 1'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Workout 2'
            on_press: root.manager.current = 'settings'  
        Button:
            text: 'Workout 3'

        MDBottomAppBar:
            md_bg_color: 1, 1, 1, 1

            MDToolbar:
                icon: "plus"
                type: "bottom"
                icon_color: 0, 0, 0, 1
                mode: "end"
                
                

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