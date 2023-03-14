from kivy.animation import Animation 
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.app import App


Builder.load_file( 'animation.kv' )


class MyLayout( Widget ):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

    def animate_it( self, widget, *args ):
        animate = Animation(size_hint = (1,1) )
        animate += Animation(size_hint = (0.5, 0.5))

        animate.start( widget )
        animate.bind( on_complete = self.my_callback )
    
    def my_callback( self, *args ):
        print( args )
        self.ids.my_label.text = 'WOOOOW!'
        

class MainApp( App ):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MainApp().run()