import socket 
client = socket.socket()
client.connect( ('160.238.145.93', 2021) )
client.send( 'PING'.encode() )
print( 'Sent: {}\nReceived: {}'.format( "PING", client.recv(1024).decode()))


# KIVY client in page 134