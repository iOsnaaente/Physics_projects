from noBackground import * 
from interface import *
from smoke import *

import numpy as np 
import pyautogui as pygui 
        
W, H = 50, 50 

# UNIÃO DO DPG COM A CLASSE SMOKE 
class dpg_smoke( Smoke ):

    particles_to_draw = [] 
    
    def __init__(self, x: int, y: int, draw_board : str, img : list, w : int, h : int ):
        super().__init__(x, y, img, w, h)
        self.img
        self.draw_board = draw_board

    def update(self):
        super().update()

    def draw( self ):
        for i in super().get_particles():
            if i.id not in self.particles_to_draw: 
                new_image = dpg.draw_image( parent = self.draw_board, texture_tag = self.img, pmin = (i.x -i.w/2, i.y-i.h), pmax = (i.x + i.w/2, i.y + i.h/2), color = (255,255,255, i.get_alpha() ) ) 
                self.particles_to_draw.append( new_image ) 
                i.set_id( new_image )
            else: 
                if i.kill_particle():
                    self.particles_to_draw.remove( i.id )
                    dpg.delete_item( i.id )
                else: 
                    dpg.configure_item( i.id, pmin = (i.x -i.w/2, i.y-i.h), pmax = (i.x + i.w/2, i.y + i.h/2), color = (255,255,255, i.get_alpha() )  )

smoke = dpg_smoke( 0, 0, 'drawlist', img = smoke_texture, w = W, h = H )
theta = 0 

## RENDER PART 
while dpg.is_dearpygui_running(): 
    dpg.render_dearpygui_frame()
    remove_bg_render("Smoke_test")
    click_through()    

    x, y = pygui.position()
    smoke.x, smoke.y = x-10, y-10 
    theta += np.radians( 5 ) 
    smoke.vector = [ np.cos( theta )*5, np.sin( theta )*5 ]

    smoke.update()
    smoke.draw()


dpg.destroy_context() 