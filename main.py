from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgageCalculatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello,\n Mortgage Calculator!", halign="center")


MortgageCalculatorApp().run()