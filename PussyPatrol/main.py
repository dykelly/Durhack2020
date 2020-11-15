import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

kivy.require('1.11.1')
Window.size = (400, 550) #So we can see what the app looks like on a phone


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

# Import other screens
from PussyPatrol.Widgets import MapWidget
from PussyPatrol.Widgets import ProfileWidget
from PussyPatrol.Widgets import NewSightingWidget
from PussyPatrol.Sighting import Sighting



class WindowManager(ScreenManager):
    pass

class MenuBar(Widget):
    pass

class MapScreen(Screen):
    pass
class NewSightingScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass


Builder.load_file('./Widgets/mapwidget.kv')
Builder.load_file('./Widgets/profilewidget.kv')
Builder.load_file('./Widgets/newsightingwidget.kv')
kv = Builder.load_file('PussyPatrol.kv')


class PussyPatrolApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    PussyPatrolApp().run()