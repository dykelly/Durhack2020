import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.image import Image, AsyncImage

username = "No one"
animal = ["bear", "cat", "dog", "horse"]
names = ["Stu", "Felix", "Rover", ""]
images = ['https://upload.wikimedia.org/wikipedia/commons/0/0b/Cat_poster_1.jpg', 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Cat_poster_1.jpg','', 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Cat_poster_1.jpg']

class ProfileWidget(BoxLayout): # boxlayout
    def __init__(self, **kwargs):
        super(ProfileWidget, self).__init__()
        mainlayout = GridLayout(rows=3, spacing=10, size_hint_y=None, width=Window.width, height=Window.height, pos = (0,100))
        mainlayout.add_widget(self.buildUpper(""))
        mainlayout.add_widget(self.buildUpper(username + "'s Profile"))
        mainlayout.add_widget(self.buildLower())
        self.add_widget(mainlayout)


    def buildLower(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None, width = Window.width)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(len(animal)):
            txt = str(i + 1) + ". Found a wild " + animal[i]
            if names[i] != "":
                txt = str(i + 1) + ". Found a " + animal[i] + " named " + names[i]
            btn = Button(text=txt, size_hint_y=None, height=40, width = Window.width)
            btn.bind(on_press=self.callback)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        return root

    def callback(self, instance):
        if instance.text.startswith('*'):
            if len(instance.children) > 0:
                instance.remove_widget(instance.children[0])
        else:
            imgsource = images[(int)(instance.text[0]) - 1]
            if imgsource != "":
                aimg = AsyncImage(source=imgsource,  height = instance.height, width = instance.height*2)
                aimg.pos = (instance.pos[0] + instance.width - aimg.width, instance.pos[1])
                instance.add_widget(aimg)
        if instance.text.startswith('*'):
            instance.text = instance.text[1:]
        else:
            instance.text = '*' + instance.text

    def buildUpper(self, txt):
        label = Label(text = txt, color = "#000000")
        #aimg = AsyncImage(source=imgsource, height=self.height - 10, width=self.width)
        #screen.add_widget(aimg)
        return label