from kivymd.tools.hotreload.app import MDApp 
from kivy.core.window import Window 
from kivy.lang import Builder 
from kivy.clock import Clock

from kivyplt.kivy_matplotlib import MatplotFigure 
from kivymd.uix.boxlayout import MDBoxLayout 

import matplotlib as mpl
import datetime  
import socket 
import json 
import sys 
import os 

PATH = os.path.dirname( __file__ )

class Ploter( MDBoxLayout ):
    if len(sys.argv) > 1: 
        IP, PORT = sys.argv[1], int(sys.argv[2])
        print( IP, PORT )
    else: 
        IP, PORT = '192.168.18.64', 80 
        print( IP, PORT )

    __debug : bool = True

    MAX_COUNT : int = 100

    sckt : socket.socket = None 
    plot : int = 0
    recv : str = ''
    vbat_plot : list = [] 
    vsol_plot : list = [] 
    x_plot    : list = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.draw() 
        Clock.schedule_interval( self.request, 1/2 )
        Clock.schedule_interval( self.render, 1/2 )

    def draw( self ):
        chart = mpl.figure.Figure( )
        self.plot = MatplotFigure( chart )
        self.add_widget( self.plot )
    
    def render( self, clock_event ):
        chart = mpl.figure.Figure( )
        chart.gca().plot_date( x = self.x_plot, y = self.vsol_plot, fmt = '-', label = 'Vsol' )
        chart.gca().plot_date( x = self.x_plot, y = self.vbat_plot, fmt = '-', label = 'Vbat' )
        self.plot = MatplotFigure( chart )
        self.clear_widgets() 
        self.add_widget( self.plot )

    def request( self, clock_value ) -> json: 
        try:         
            self.sckt = socket.socket()
            self.sckt.settimeout( 0.15 )
            self.sckt.connect( (self.IP, self.PORT) )
            data_send = 'GET / HTTP/1.1\r\nHost:{}:{}\r\n\r\n'.format(self.IP, self.PORT)
            self.sckt.send( data_send.encode() )
            data_rec = self.sckt.recv( 4096 )
            if 'OK' in data_rec.decode():
                data_rec = self.sckt.recv( 4096 )
                data_rec = data_rec.decode().replace('\r\nContent-type:text/html\r\n\r\n', '' ).replace('\r\n', '')
                data_json = json.loads( data_rec )
                if self.__debug: print( data_json )
            else: 
                data_json = False 
        except socket.error as e :
            data_json = False
            if self.__debug: print( e ) 
        self.sckt.close()
        if type(data_json) == dict: 
            self.x_plot.append( datetime.datetime.now() )
            self.vbat_plot.append( data_json['Vbat'])
            self.vsol_plot.append( data_json['Vsol'])
            while len(self.x_plot   ) > self.MAX_COUNT:
                self.x_plot.pop(0)
            while len(self.vbat_plot) > self.MAX_COUNT:
                self.vbat_plot.pop(0)
            while len(self.vsol_plot) > self.MAX_COUNT:
                self.vsol_plot.pop(0)
                

class Ploter_APP( MDApp ):
    KV_FILES = [
        PATH + '/ploter.kv'
    ]
    
    PAGE : str = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build_app(self):
        Window.bind( on_key_down = self.on_keyboard_down )
        self.PAGE = Builder.load_file( self.KV_FILES[0] )
        return self.PAGE

    def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
        if "meta" in modifiers or "ctrl" in modifiers and text == "r":
            self.rebuild()


Ploter_APP().run()