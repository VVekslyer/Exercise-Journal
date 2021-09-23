# In order to run the app, make sure that pip is updated in the Shell console.
# Type in "pip install --upgrade pip" and Enter in the Shell console.

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.lang import Builder

# Designate our .kv design file
Builder.load_file('main.kv')

class Layout(Widget):
  pass

# Defining the main app class, which returns a hello world label.
class Main(App):
    def build(self):
        return Label(text="LETS GET IT !", font_size=28)


# Here our class is initialized
# and its run() method is called.
# This starts our Kivy app.
if __name__ == '__main__':
  Main().run()
