import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import Screen

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

marker_img = "resources/mapmarker.png"

class MapWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MapWidget, self).__init__(**kwargs)
        self.map = MapView(zoom=17, lat=54.768, lon=-1.5905)
        self.add_widget(self.map)
        self.add_marker(54.768, -1.5905)

    def add_marker(self, lat, lon):
        marker = MapMarker()
        marker.lat = lat
        marker.lon = lon
        marker.source = marker_img
        self.map.add_marker(marker)



