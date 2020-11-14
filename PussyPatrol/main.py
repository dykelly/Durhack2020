import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class PussyPatrol(Widget):
    pass


class PussyPatrolApp(App):
    def build(self):
        return PussyPatrol()


if __name__ == '__main__':
    PussyPatrolApp().run()
