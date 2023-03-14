from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.app import App


Builder.load_file( 'buttomImage.kv' )

class MyLayout( Widget ):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

    def say_my_name( self, name ):
        self.ids.my_label.text = f'My name is {name}'


class MainApp( App ):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MainApp().run()