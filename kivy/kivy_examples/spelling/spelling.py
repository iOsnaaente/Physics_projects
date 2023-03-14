from kivy.core.spelling import Spelling
from kivy.uix.widget import Widget
from kivy.lang import Builder 
from kivy.app import App



Builder.load_file( 'spelling.kv' )

class MyLayout( Widget ):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

    def press_submit( self ): 
        s = Spelling()
        s.select_language('en_US')
        
        word = self.ids.word_input.text 
        option = s.suggest( word )
        
        big_word = ''
        for opt in option:
            big_word += opt + ', '

        self.ids.word_label.text = f'Suggested: {big_word[:-1]}'


class MainApp( App ):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MainApp().run()