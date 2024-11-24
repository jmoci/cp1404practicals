from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_CONSTANT = 1.60934

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
        """increment or decrement text field value based on sign argument"""
        try:
            self.root.ids.input_miles.text = str(float(self.root.ids.input_miles.text)+sign)
        except ValueError:
            self.root.ids.input_miles.text = f"{float(sign):.2}"

    def handle_convert_mi_to_km(self, miles):
        """update message to a string representing the result of miles argument converted to kilometers"""
        try:
            result = float(miles)*MILES_TO_KM_CONSTANT
            self.message = str(result)
        except ValueError:
            self.message = "0"

MilesToKMApp().run()