import dearpygui.dearpygui as dpg 

from ctypes import c_int
import win32gui
import win32con
import ctypes

dwm = ctypes.windll.dwmapi
class MARGINS(ctypes.Structure):
  _fields_ = [("cxLeftWidth", c_int),
              ("cxRightWidth", c_int),
              ("cyTopHeight", c_int),
              ("cyBottomHeight", c_int)
             ]


dpg.create_context()
dpg.create_viewport( title = 'viewport', clear_color = [0.0,0.0,0.0,0.0], always_on_top = True, decorated = True  )

with dpg.window( tag = 'main_window', no_background = False, no_title_bar = True, no_resize = True ):
    pass 


dpg.setup_dearpygui()
dpg.toggle_viewport_fullscreen()
dpg.show_viewport()

while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

    hwnd = win32gui.FindWindow( None, "viewport" )
    margins = MARGINS(-1, -1,-1, -1)
    dwm.DwmExtendFrameIntoClientArea(hwnd, margins)
    # Enable this for click through otherwise always overtop
    # win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT )

dpg.destroy_context()
