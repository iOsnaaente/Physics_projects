from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.app import App


Builder.load_file( 'image.kv' )

class MyLayout( Widget ):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

    def selected( self, file_selected ): 
        try:
            self.ids.my_image.source = file_selected[0]
            print( file_selected )
        except:
            pass 



class MainApp( App ):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MainApp().run()