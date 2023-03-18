import socket 
import json 
import sys 

'''
USAGE: 
    $ python3 test_sck.py 'XXX.XXX.XXX.XXX' 1234
'''

IP   = sys.argv[1]
PORT = int(sys.argv[2])

sckt = socket.socket() 
sckt.settimeout( 1 )

def request( sckt : socket.socket, __debug : bool = False ) -> json: 
    try: 
        sckt.connect( (IP, PORT) )
        data_send = 'GET / HTTP/1.1\r\nHost:{}:{}\r\n\r\n'.format(IP, PORT)
        sckt.send( data_send.encode() )
        data_rec = sckt.recv( 4096 )
        if 'OK' in data_rec.decode():
            data_rec = sckt.recv( 4096 )
            data_rec = data_rec.decode().replace('\r\nContent-type:text/html\r\n\r\n', '' ).replace('\r\n', '')
            data_json = json.loads( data_rec )
        else: 
            data_json = json.loads( '{}' ) 
    except socket.error as e :
        data_json = json.loads( '{}' ) 
        if __debug: print( e ) 
    sckt.close()
    return data_json 

data = request( sckt )

vbat = data['Vbat']
vsol = data['Vsol']

print( vbat, vsol )