from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesToKMApp(App):
    """ MilesToKMApp is a Kivy App for converting miles to kilometers """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Mi to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

MilesToKMApp().run()