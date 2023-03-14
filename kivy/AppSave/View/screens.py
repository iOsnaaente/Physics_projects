# Login 
from Model.login import LoginModel 
from Controller.login import LoginController 
# Home
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController


screens = {
    "login": {
        "model": LoginModel,
        "controller": LoginController
    },
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },
}