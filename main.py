# In order to run the app, make sure that pip is updated in the Shell console.
# Type in "pip install --upgrade pip" and Enter in the Shell console.

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

ui = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'vitaly540@gmail.com'
        MDLabel:
            text: 'Hello, world!'

"""

class Main(MDApp):
    def build(self):
        screen = Builder.load_string(ui)
        return screen


# Here our class is initialized
# and its run() method is called.
# This starts our Kivy app.
if __name__ == '__main__':
  Main().run()
