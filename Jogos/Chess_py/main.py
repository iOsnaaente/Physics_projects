import dearpygui.dearpygui as dpg 

from os import path 

PATH = path.dirname(__file__)
SMALL_ICO = PATH + '/public/small_ico.ico'
LARGE_ICO = PATH + '/public/large_ico.ico'

dpg.create_context()

## MAIN WINDOW
with dpg.window( tag = 'mainWindow', no_close=True, no_collapse=True, no_move=True, no_scrollbar=True, no_title_bar=True ):
    with dpg.menu_bar():
        dpg.add_menu_item( tag = "MenuInicio"  , label='Inicio'   )
        dpg.add_menu_item( tag = "MenuNovoJogo", label='Novo Jogo')
        dpg.add_menu_item( tag = "MenuPlacar"  , label='Placar'   )
        dpg.add_menu_item( tag = "MenuSair"    , label='Sair'     )

def theme_board( who : str , black : bool ):
    with dpg.theme() as theme_color : 
        if black: 
            dpg.add_theme_color( dpg.mvThemeCol_WindowBg, [20,211,52,240], category = dpg.mvThemeCat_Core )
        else: 
            dpg.add_theme_color( dpg.mvThemeCol_WindowBg, [20,20,30,240], category = dpg.mvThemeCat_Core )
    dpg.set_item_theme(who, theme_color)
            

with dpg.window( tag = 'gameBoard', width=1080, height=1080, pos=[10,25], no_close=True, no_collapse=True, no_move=True, no_scrollbar=True, no_title_bar=True  ):
   for n,i in enumerate(['a','b','c','d','e','f','g','h']): 
       for j in range(8):
            w, h = dpg.get_item_width('gameBoard')/8, dpg.get_item_height('gameBoard')/8
            dpg.window(tag='gameTile{}{}'.format(i, j), width=w, height=h, pos=[n*32, j*32] )
            if n*j%2 == 0 : 
               theme_board( 'gameTile{}{}'.format(i,j), False )
            else : 
               theme_board( 'gameTile{}{}'.format(i,j), True )




## CALLBACKS 
def resize_windows( sender, data, user ):
    nw, nh = data[2], data[3]
    print( nw, nh )

def mouse_move(sender, data, user ): 
    dpg.configure_item('mouseStatus', default_value = data )
    print(data)


## INIT CONFIGURATIONS 
dpg.create_viewport(
    title='DearChess pyGUI', 
    width     = 600, 
    min_width = 1000,
    height    = 200, 
    min_height= 800, 
    small_icon= SMALL_ICO, 
    large_icon= LARGE_ICO )

dpg.setup_dearpygui()
dpg.set_primary_window("mainWindow", True)

dpg.set_viewport_resize_callback( resize_windows )
dpg.maximize_viewport() 
dpg.show_viewport()

dpg.start_dearpygui()




## RENDER PART 
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

dpg.destroy_context()