import importlib

import View.Login.login as login

importlib.reload( login )

class LoginController:
    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = login(controller=self, model=self.model)

    def get_view(self) -> login:
        return self.view
