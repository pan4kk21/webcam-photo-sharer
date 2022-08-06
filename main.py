from photo_sharer import PhotoSharer

import time

import webbrowser

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

Builder.load_file("frontend.kv")


class WebcamScreen(Screen):

    def start(self):
        self.ids.camera.play = True
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera.texture = None

    def capture(self):
        self.filepath = f"files/{time.strftime('%Y.%m.%d-%H:%M:%S')}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "imagescreen"
        self.manager.current_screen.ids.image.source = self.filepath


class ImageScreen(Screen):

    alert_message = "[font=GoogleSans-Medium]Create a Link First![/font]"

    def create_link(self):
        filepath = App.get_running_app().root.ids.webcamscreen.filepath
        photo_sharer = PhotoSharer(filepath=filepath)
        self.url = photo_sharer.share()
        self.ids.filelink.text = f"[font=GoogleSans-Medium]{self.url}[/font]"

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.filelink.text = self.alert_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.filelink.text = self.alert_message



class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        self.title = "Webcam Photo Sharer"
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
