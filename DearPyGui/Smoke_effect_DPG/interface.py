import dearpygui.dearpygui as dpg 
import os 

PATH = os.path.dirname( __file__ )


# INIT DPG CONTEXT AND VIEWPORT 
dpg.create_context()
dpg.create_viewport(  
    title = 'Smoke_test',
    clear_color = [0.0,0.0,0.0,0.0], 
    always_on_top = True, 
    decorated = False  )


# TEXTURE REGISTRY 
with dpg.texture_registry( ) as texture_registry: 
    w, h, c, d = dpg.load_image( PATH + '/images/smoke.png' )
    smoke_texture = dpg.add_raw_texture( w, h, d )


# HANDLERS 
with dpg.handler_registry() as handler_registry: 
    dpg.add_key_down_handler( dpg.mvKey_Escape, callback = dpg.destroy_context )
    dpg.add_key_down_handler( dpg.mvKey_Q     , callback = dpg.destroy_context )
    # lMouse_callback = dpg.add_mouse_click_handler( dpg.mvMouseButton_Left, callback = lambda : print() )
    # rMouse_callback = dpg.add_mouse_click_handler( dpg.mvMouseButton_Right, callback = lambda : print() )


## MAIN WINDOW
with dpg.window( tag = 'main_window', width = 2000, height = 1500, no_background = True, no_scrollbar = True, no_move = True, no_title_bar = True, no_resize = True ):
    dpg.add_drawlist( tag = 'drawlist', width = 500, height = 500 )


# VIEWPORT RESIZE CALLBACK 
def win_resize( sender, data, user): 
    dpg.configure_item( 'main_window',width = data[0], height = data[1] )
    dpg.configure_item( 'drawlist',   width = data[2], height = data[3] )


## INIT CONFIGURATIONS 
dpg.setup_dearpygui()
dpg.set_viewport_resize_callback( win_resize )
dpg.toggle_viewport_fullscreen()
dpg.set_viewport_always_top( True )
dpg.show_viewport()
