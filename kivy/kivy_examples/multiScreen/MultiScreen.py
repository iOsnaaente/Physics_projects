from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.app import App

# Especify which screens we will use 
class MainScreen( Screen):
    pass 

class SecondScreen( Screen ):
    pass 

class Gerente ( ScreenManager ):
    pass 



build_screen = Builder.load_file( 'MultiScreen.kv' )

class MainApp( App ):
    def build(self):
        return build_screen

if __name__ == '__main__':
    MainApp().run()