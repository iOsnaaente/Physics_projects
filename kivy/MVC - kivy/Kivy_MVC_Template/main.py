from Controller.myscreen import MyScreenController
from Model.myscreen import MyScreenModel
from kivymd.app import MDApp


class APP(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        self.model = MyScreenModel()
        self.controller = MyScreenController(self.model)


    def build(self):
        return self.controller.get_screen()


APP().run()
