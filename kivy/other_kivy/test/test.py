from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.app import App


Builder.load_file( 'slider.kv' )

class MyLayout( Widget ):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)


class MainApp( App ):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MainApp().run()