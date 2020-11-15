import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
import breeds_manager as bm
import identified_manager as im
import master_manager as mm
import pictures_manager as pm
import sightings_manager as sm
import users_manager as um

kivy.require('1.11.1')
Window.size = (400, 550) #So we can see what the app looks like on a phone


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# Import other screens
from Widgets import MapWidget
from Widgets import ProfileWidget
from Widgets import NewSightingWidget
from Sighting import Sighting


class WindowManager(ScreenManager):
    pass

class MenuBar(Widget):
    pass

class MapScreen(Screen):
    def UpdateMap(lat=54.768, lon=-1.5905, radius=5, time_days=31, animal_type='cat'):
        # get current position
        # send search query to database
        # database returns a list of sightings
        # clear previous sightings from map
        # add new sightings and center map on lat,lon with a radius = radius

        pass
    pass
class NewSightingScreen(Screen):

    pass
class ProfileScreen(Screen):
    pass





Builder.load_file('./Widgets/mapwidget.kv')
Builder.load_file('./Widgets/profilewidget.kv')
Builder.load_file('./Widgets/newsightingwidget.kv')
kv = Builder.load_file('CatCruiser.kv')


class CatCruiserApp(App):
    # def __init__(self):
    #     super(CatCruiserApp, self).__init__()
    #     self.screen_manager = WindowManager
    def build(self):
        return kv



if __name__ == '__main__':
    CatCruiserApp().run()