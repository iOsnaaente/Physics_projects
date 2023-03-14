import dearpygui.dearpygui as dpg 
from twenties import * 

import os 

PATH = os.path.dirname( __file__ ).removesuffix( 'twenties_game.py' )
COLLUMS = 5
ROWS = 5

TABLE = build_table( ROWS, COLLUMS )
TABLE = spaw_new_turn( TABLE, ROWS )
  

# INICIO DO CONTEXTO DO DPG 
dpg.create_context()
dpg.create_viewport( title = 'Twenties', min_width = 800, min_height = 600 )
dpg.setup_dearpygui()


# FUNÇÕES MAIN
def resize_main( ):
    pass 

def render_main( ):
    pass

def init_main():
    with dpg.window( label = 'Main Window', tag = 'mainWindow', autosize = True ):
        #with dpg.window(tag = 'MainView', width = -1, height = -1, pos = [10, 25], no_close = True, no_title_bar = True, no_resize = True):
        for x in range( ROWS ):
            with dpg.group( horizontal = True ):
                for y in range( COLLUMS ) :
                    dpg.add_button( tag = int( str(x)+str(y) ), label = TABLE[x][y], width = 150, height = 150 )

       

def att_positions( sender, user, data ):
    pass 

def new_move( sender, user, data ):
    pass 


# CONSTRUÇÃO DO ESCOPO MAIN 
init_main() 

dpg.add_key_press_handler( key = dpg.mvKey_S, callback = lambda s, d, u: print( s,d,u) ) 

#with dpg.font_registry() as font_def: 
#    font = dpg.add_font( PATH  + '\\PressStart.ttf', 25)

with dpg.theme() as themes:
    with dpg.theme_component( dpg.mvAll ):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (250, 250, 250), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (33, 33, 33), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (33, 33, 33), category=dpg.mvThemeCat_Core)
        #dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (100,255,100), category = dpg.mvThemeCat_Core)

# Bigger than 1 
with dpg.theme() as theme5:
    with dpg.theme_component( dpg.mvAll ):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (200, 255, 200), category=dpg.mvThemeCat_Core)




dpg.bind_theme( themes )
#dpg.bind_font( font )

# CONFIGURAÇÕES 
dpg.set_primary_window          ( 'mainWindow', True )
dpg.set_viewport_resize_callback( resize_main        )
dpg.maximize_viewport           (                    ) 

# INICIAR AS VIEWS DO DPG
dpg.show_viewport( )


# LAÇO DE RENDERIZAÇÃO DO DPG
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame() 

    moves = 'b' #input( 'Jogo: ' )
    moved = False
    for move in moves:
        if   move == 'a':   
            TABLE = move_left( TABLE )
            moved = True 
        elif move == 's':   
            TABLE = move_down( TABLE )
            moved = True 
        elif move == 'd':   
            TABLE = move_right( TABLE )
            moved = True 
        elif move == 'w':   
            TABLE = move_up( TABLE )
            moved = True 
        else:               continue
    
    TABLE = check_twenty( TABLE )
    TABLE = check_twenty_five( TABLE )

    if check_end_game( TABLE ): break
    if moved:    TABLE = spaw_new_turn( TABLE, 2)
    
    print_game( TABLE )

print( "Fim de jogo. Pontuação: %f " %SCORE)