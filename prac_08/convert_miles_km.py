from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class MilesToKMApp(App):
    """ MilesToKMApp is a Kivy App for converting miles to kilometers """

    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 200)
        self.title = "Convert Mi to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to km"
        return self.root

    def handle_increment(self,sign):
        try:
            self.root.ids.input_miles.text = str(float(self.root.ids.input_miles.text)+sign)
        except ValueError:
            pass
    def handle_convert_mi_to_km(self, miles):
        try:
            result = float(miles)*1.60934
            self.message = str(result)
        except ValueError:
            pass

MilesToKMApp().run()