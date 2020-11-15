import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import Screen
import master_manager as mm

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

marker_img = "resources/mapmarker.png"


class SightingTooltip(BoxLayout):
    def __init__(self, touch_position, sighting, **kwargs):
        self.canvas_pos = (touch_position.x, touch_position.y)
        print(self.pos)
        self.layout_pos = (touch_position.x+80, touch_position.y+50)
        super(SightingTooltip, self).__init__()
        # LabelAnName()


# class LabelAnName(Label):
#     def __init__(self):
#         super(LabelAnName, self).__init__(text="Mad ", color=(0, 0, 0, 1))
        # self.text = "Mad boi"

class LabelDesc(Label):
    pass


class SightingMarker(MapMarker):
    current_tooltip = None

    def __init__(self, sighting_id, **kwargs):
        super(SightingMarker, self).__init__()
        self.sighting_id = sighting_id

    def on_press(self):
        print("Creating tooltip")
        if self.current_tooltip:
            self.remove_widget(self.current_tooltip)
            self.current_tooltip = None
        else:
            print(self)
            tooltip = SightingTooltip(self.last_touch, None)
            self.add_widget(tooltip)
            self.current_tooltip = tooltip



class MapWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MapWidget, self).__init__(**kwargs)
        self.map = MapView(zoom=10, lat=54.768, lon=-1.5905)
        self.add_widget(self.map)
        self.add_sighting(54.768, -1.5905, "MARKERIDTEST")
        self.get_nearby_sightings()

    def add_sighting(self, lat, lon, id):
        marker = SightingMarker(id)
        marker.lat = lat
        marker.lon = lon
        marker.source = marker_img
        self.map.add_marker(marker)

    def move_to(self, lat, lon):
        self.map.lat = lat
        self.map.lon = lon

    def get_nearby_sightings(self):
        # print(f'getting sightings near {self.map.lat} {self.map.lon}')
        nearby_sightings = mm.hot_puss_in_your_area(self.map.lat, self.map.lon)
        for sighting in nearby_sightings:
            # print(sighting)
            self.add_sighting(sighting.Lat, sighting.Lon, sighting.Asid)
            

    def on_map_relocated(self):
        print("Map moved")
