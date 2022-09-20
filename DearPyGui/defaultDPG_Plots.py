import dearpygui.dearpygui as dpg 

import numpy as np 

NUM_PONTOS_X = 1000
NUM_PONTOS_Y = 1000

NUM_POINTS = 1000

dpg.create_context()

## CALLBACKS 
def resize_windows( sender, data, user ):
    dpg.configure_item( item = 'simulation' ,  pos = [  25,  25 ], height = 550, width = 750 )
    dpg.configure_item( item = 'data_x'     ,  pos = [  25, 600 ], height = 200, width = 750 )
    dpg.configure_item( item = 'data_y'     ,  pos = [ 790,  25 ], height = 550, width = 220 )
    dpg.configure_item( item = 'inputs'     ,  pos = [ 1025,  25 ], height = 775, width = 425 )


def func_button( sender, data, user ):
    print(  sender, data, user )

## MAIN WINDOW
with dpg.window( tag = 'mainWindow', no_close = True, no_collapse = True, no_move = True, no_scrollbar = True, no_title_bar = True ):

    # Janela de simulação
    with dpg.window( tag = 'simulation', no_close = True, no_collapse = True, no_move = True, no_scrollbar = True, no_title_bar = True ): 
        dpg.add_drawlist( tag = 'drawing', width = 750, height = 550, pos = [10,10] )

        for i in range( NUM_POINTS ):
            #dpg.draw_circle( parent= 'drawing', tag = 1205+i, radius = np.random.randint(2,10), center=[np.random.randint(10,690),np.random.randint(10,490)], color=[100,220,0,255], fill=[255,230,5,255] )
            dpg.draw_circle( parent= 'drawing', tag = 1205+i, radius = np.random.randint(2,10), center=[ 690/2 , 490/2 ], color=[100,220,0,255], fill=[255,230,5,255] )
        

    # Janela de grafico X
    with dpg.window( tag = 'data_x', no_close = True, no_collapse = True, no_move = True, no_scrollbar = True, no_title_bar = True ):
        with dpg.plot( tag = 'plotter_data_x', label = 'Contagem X', width = -1, height = -1, anti_aliased = True, no_title = True ):
            dpg.add_plot_legend()
            with dpg.plot_axis( dpg.mvXAxis, tag = 'axis_data_points_x' ):
                dpg.set_axis_limits( 'axis_data_points_x', ymin = 0, ymax = NUM_PONTOS_X )
            with dpg.plot_axis( dpg.mvYAxis, tag = 'axis_data_count_x' ):
                dpg.set_axis_limits( 'axis_data_count_x', ymin = 0, ymax = NUM_PONTOS_Y )     
                dpg.add_line_series([ ], [ ], tag = 'series_data_count_x', parent = 'axis_data_count_x' )
                
    # Janela de Gráfico Y 
    with dpg.window( tag = 'data_y', no_close = True, no_collapse = True, no_move = True, no_scrollbar = True, no_title_bar = True ):
        with dpg.plot( tag = 'plotter_data_y', label = 'Contagem Y', width = -1, height = -1, anti_aliased = True, no_title = True ):
            dpg.add_plot_legend()
            with dpg.plot_axis( dpg.mvXAxis, tag = 'axis_data_points_y' ):
                dpg.set_axis_limits( 'axis_data_points_y', ymin = 0, ymax = NUM_PONTOS_X )
            with dpg.plot_axis( dpg.mvYAxis, tag = 'axis_data_count_y' ):
                dpg.set_axis_limits( 'axis_data_count_y', ymin = 0, ymax = NUM_PONTOS_Y )     
                dpg.add_line_series([ ], [ ], tag = 'series_data_count_y', parent = 'axis_data_count_y' )
    
    
    # Janela de Gráfico Y 
    with dpg.window( tag = 'inputs', no_close = True, no_collapse = True, no_move = True, no_scrollbar = True, no_title_bar = True ):
        dpg.add_button( label = 'meu botão', width = 250, height = 250, callback = func_button  )

    
    dpg.configure_item( item = 'simulation' ,  pos = [  25,  25 ], height = 550, width = 750 )
    dpg.configure_item( item = 'data_x'     ,  pos = [  25, 600 ], height = 200, width = 750 )
    dpg.configure_item( item = 'data_y'     ,  pos = [ 790,  25 ], height = 550, width = 220 )
    dpg.configure_item( item = 'inputs'     ,  pos = [ 1025,  25 ], height = 775, width = 425 )


with dpg.handler_registry() as hand: 
    dpg.add_key_down_handler( dpg.mvKey_A, callback = lambda sender, data, user : print('tecla a pressionada' ))

## INIT CONFIGURATIONS 
dpg.create_viewport( title = 'Simulação de movimento aleatório', width = 600, min_width = 1000, height = 200,  min_height = 800  )

dpg.setup_dearpygui()
dpg.set_primary_window("mainWindow", True)

dpg.set_viewport_resize_callback( resize_windows )
dpg.maximize_viewport() 
dpg.show_viewport()



# HANDLERS 
with dpg.handler_registry(): 
    pass


X_MAX = 690
Y_MAX = 740 
R_MAX = 8

SERIES = [ 0 for i in range( X_MAX ) ] 


## RENDER PART 
while dpg.is_dearpygui_running(): 
    dpg.render_dearpygui_frame()
    
    for i in range( NUM_POINTS ):
        r  = np.random.randint(-1, 2)
        x, y  = np.random.randint(-5,6,), np.random.randint(-5,6)
 
        dr = dpg.get_item_configuration(1205+i)['radius'] + r 
        dx = dpg.get_item_configuration( 1205+i)['center'][0] + x
        dy = dpg.get_item_configuration( 1205+i)['center'][1] + y 
 
        if dx > X_MAX or dx < 0: dx -= x
        if dy > Y_MAX or dy < 0: dy -= y
        if dr > R_MAX or dr < 2: dr -= r 

        
        dpg.configure_item( item = 1205+i, 
                            radius = dr,
                            center = [dx, dy]
        )


dpg.destroy_context()