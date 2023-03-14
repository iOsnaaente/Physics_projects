from View.base_screen import BaseScreenView

from kivy.lang import Builder 

class Login( BaseScreenView ):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget( Builder.load_file('login.kv') )