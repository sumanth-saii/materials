from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from suppoter import kv
from kivy.core.window import Window


class Mainscreen(Screen):
    pass


class Secondscreen(Screen):
    pass


class windowmanager(ScreenManager):
    pass


Window.size = (360, 600)


class demo(MDApp):
    def build(self):
        self.theme_cls.primary_palette= 'Green'
        k = Builder.load_string(kv)
        return k


demo().run()
