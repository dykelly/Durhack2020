import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# Import other screens
from Widgets import MapWidget
from Widgets import ProfileWidget

Builder.load_file('./Widgets/mapwidget.kv')
Builder.load_file('./Widgets/profilewidget.kv')

class PussyPatrol(Screen):
    pass


class PussyPatrolApp(App):
    def build(self):
        return PussyPatrol()


if __name__ == '__main__':
    PussyPatrolApp().run()
