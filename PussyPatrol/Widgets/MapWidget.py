import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import Screen

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MapWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MapWidget, self).__init__(**kwargs)
        self.add_widget(MapView(zoom=11, lat=40, lon=20))

