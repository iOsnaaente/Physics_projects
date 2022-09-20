import dearpygui.dearpygui as dpg 
import os 

PATH = os.path.dirname( __file__ )

dpg.create_context()
dpg.create_viewport( title = '', width = 600, min_width = 1000, height = 200,  min_height = 800  )


# TEXTURE REGISTRY 
with dpg.texture_registry( ) as texture_registry: 
    w, h, c, d = dpg.load_image( PATH + '\\smoke.png' )
    smoke_texture = dpg.add_raw_texture( w, h, d )

# HANDLERS 
with dpg.handler_registry() as handler_registry: 
    dpg.add_key_down_handler( dpg.mvKey_A, callback = lambda sender, data, user : print('Tecla A pressionada' ))

# VALUE REGISTRY 
with dpg.value_registry() as value_registry: 
    pass 

## MAIN WINDOW
with dpg.window( tag = 'mainWindow', no_close = True, no_collapse = True, no_move = True, no_scrollbar = True, no_title_bar = True ):
    dpg.add_drawlist( tag = 'drawlist', width = -1, height = -1 )


## RESIZE CALLBACK  
def resize_windows( sender, data, user ):
    pass 


## INIT CONFIGURATIONS 
dpg.setup_dearpygui()
dpg.set_primary_window("main_window", True )
dpg.set_viewport_resize_callback( resize_windows )
dpg.maximize_viewport() 
dpg.show_viewport()