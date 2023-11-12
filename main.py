from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class ScrButton(Button):
    def __init__(self, screen, direction="right", goal="main", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical")
        hl = BoxLayout()
        btn1 = ScrButton(self, direction="left", goal="first", text = "First screen",
                         size_hint = (0.5, 0.5))
        vl.add_widget(btn1)
        btn2 = ScrButton(self, direction="left", goal="second", text = "Second screen",
                         size_hint=(0.5, 0.5))
        vl.add_widget(btn2)
        btn3 = ScrButton(self, direction="left", goal="third", text = "Third screen",
                         size_hint=(0.5, 0.5))
        vl.add_widget(btn3)
        btn4 = ScrButton(self, direction="left", goal="fourth", text = "Fourth screen",
                         size_hint=(0.5, 0.5))
        vl.add_widget(btn4)
        text = Label(text = "Виберіть екран", pos_hint = {"center_x": 0.75, "center_y": 0.5})
        self.add_widget(vl)
        self.add_widget(text)
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", size_hint = (0.5,0.5),
                       pos_hint = {"center_x": 0.5, "center_y": 0.5})
        btn = ScrButton(self, direction = "right", goal = "main", text = "To main screen")
        vl.add_widget(btn)
        self.add_widget(vl)
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", size_hint = (0.5,0.5),
                       pos_hint = {"center_x": 0.5, "center_y": 0.5})
        btn = ScrButton(self, direction = "right", goal = "main", text = "To main screen")
        vl.add_widget(btn)
        self.add_widget(vl)

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", size_hint = (0.5,0.5),
                       pos_hint = {"center_x": 0.5, "center_y": 0.5})
        btn = ScrButton(self, direction = "right", goal = "main", text = "To main screen")
        vl.add_widget(btn)
        self.add_widget(vl)

class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation="vertical", size_hint = (0.5,0.5),
                       pos_hint = {"center_x": 0.5, "center_y": 0.5})
        btn = ScrButton(self, direction = "right", goal = "main", text = "To main screen")
        vl.add_widget(btn)
        self.add_widget(vl)


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name = "main"))
        screen_manager.add_widget(FirstScreen(name = "first"))
        screen_manager.add_widget(SecondScreen(name = "second"))
        screen_manager.add_widget(ThirdScreen(name = "third"))
        screen_manager.add_widget(FourthScreen(name = "fourth"))
        return screen_manager
MyApp().run()

