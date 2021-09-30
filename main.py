# Make sure pip installer is updated to latest version in order to run.
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Window.size = (410, 730)

Builder.load_string("""
<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Vitaliy Vekslyer'
            font_name: 'assets/fonts/Inter-Medium.ttf'
            left_action_items: [["account-circle"]]
            right_action_items: [["dots-vertical"]]
            md_bg_color: app.theme_cls.bg_light
            specific_text_color: (0,0,0,1)
            elevation: 0  

        MDBottomNavigation:
            text_color_active: 1, 0, 0, 1
            panel_color: 1, 1, 1, 1

            MDBottomNavigationItem:
                name: "screen 1"
                text: "Home"
                icon: 'home'     

                BoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Home'
                        text_size: self.size
                        valign: 'top'
                        halign: 'left'
                        markup: True
                        padding_x: '24dp'
                        padding_y: '12dp'
                        text_color: (0,0,0,1)
                        font_style: 'H4'
                        font_name: 'assets/fonts/Inter-SemiBold.ttf'
                    MDFloatingActionButtonSpeedDial:
                        rotation_root_button: True
                        data: app.data
                        bg_color_root_button: (0,0,0,1)
                        bg_color_stack_button: (0,0,0,1)
                        bg_color_stack_label: (0,0,0,1)
                        bg_hint_color: (0,0,0,1)
       

            MDBottomNavigationItem:
                name: "screen 2"
                text: "Workout"
                icon: 'lightning-bolt'

                BoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Workout'
                        text_size: self.size
                        valign: 'top'
                        halign: 'left'
                        markup: True
                        padding_x: '24dp'
                        padding_y: '12dp'
                        text_color: (0,0,0,1)
                        font_style: 'H4'
                        font_name: 'assets/fonts/Inter-SemiBold.ttf'
                    MDFloatingActionButtonSpeedDial:
                        rotation_root_button: True
                        data: app.data
                        bg_color_root_button: (0,0,0,1)
                        bg_color_stack_button: (0,0,0,1)
                        label_text_color: (1,1,1,1)

            MDBottomNavigationItem:
                name: "screen 3"
                text: "Progress"
                icon: 'chart-bar'

                BoxLayout:
                    orientation: 'vertical'
                    MDLabel:
                        text: 'Progress'
                        text_size: self.size
                        valign: 'top'
                        halign: 'left'
                        markup: True
                        padding_x: '24dp'
                        padding_y: '12dp'
                        text_color: (0,0,0,1)
                        font_style: 'H4'
                        font_name: 'assets/fonts/Inter-SemiBold.ttf'

                
                
                

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to home'
            on_press: root.manager.current = 'home'
""")

# Declare both screens
class HomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SettingsScreen(Screen):
    pass

class App(MDApp):

    data = {
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