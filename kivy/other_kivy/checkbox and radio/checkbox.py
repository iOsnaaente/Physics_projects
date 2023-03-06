from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.app import App

Builder.load_file( 'checkbox.kv' )


class MyLayout( Widget ):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        
        self.sabores = [ ]


    def checkbox_click( self, instance, value, user):
        if value: 
            self.sabores.append(user)
        else: 
            if user in self.sabores:
                self.sabores.remove( user )


    def pizza_size( self, instance, value, user):
        sabores = ''
        for sabor in self.sabores:
            sabores += sabor + ' e '
        sabores = sabores[:-2]
        # self.ids.choice.text = 'Escolhido pizza{} de {} {}'.format('s' if len(self.sabores)>1 else '', sabores, user  )



class MainApp( App ):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MainApp().run()