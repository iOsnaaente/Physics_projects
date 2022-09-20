import win32gui
import win32con
import ctypes

from ctypes import c_int

dwm = ctypes.windll.dwmapi
hwnd = None 

class MARGINS(ctypes.Structure):
  _fields_ = [("cxLeftWidth", c_int),
              ("cxRightWidth", c_int),
              ("cyTopHeight", c_int),
              ("cyBottomHeight", c_int)
             ]

def remove_bg_render( name ):
    global hwnd 
    hwnd = win32gui.FindWindow(None, name )
    margins = MARGINS(-1, -1,-1, -1)
    dwm.DwmExtendFrameIntoClientArea(hwnd, margins)

# Enable this for click through otherwise always overtop
def click_through( ):
    global hwnd 
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT )