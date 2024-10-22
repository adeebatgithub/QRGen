from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from qrcode_generator import QRGenerator


class MainScreen(BoxLayout):

    def generate(self):
        qr_data = self.ids.qr_data.text
        if not qr_data:
            self.ids.message.text = "Please enter valid data."
            return

        self.ids.message.text = "Please enter valid data."
        qr = QRGenerator(version=2, box_size=10, border=2)
        qr.save(qr_data)
        self.ids.message.text = "QR code generated"


class Main(App):
    def build(self):
        self.icon = "icon.ico"
        self.title = "QR Code Generator"
        return MainScreen()


if __name__ == '__main__':
    Main().run()
