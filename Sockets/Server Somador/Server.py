import _thread 
import socket 
import struct 

HOST = 'localhost'
PORT = 12345

# Número máximo de clientes permitidos 
MAX_CONNECTIONS = 5
# Inicia o arquivo socket 
server = socket.socket() 
# Inicia a escuta no endereço 
server.bind( (HOST, PORT) )
# Define o numero máximo de clientes que podem estar 
#   conectados simultaneamente 
server.listen( MAX_CONNECTIONS ) 


# Função que fará a soma 
def calculator( msg ): 
    operators = [ '+', '-', '*', '/' ]
    operations = []
    numbers = []
    A = ''
    for char in msg: 
        if char not in operators:
            A += char 
        else:
            pass 


# Função que irá rodar de forma paralela as solicitações
#   de cada cliente conectado. 
def multi_threaded_client( connection : socket ) -> None:
    while True:
        # Aguarda o recebimento de dados 
        data = connection.recv(2048).decode()
        if data:
            res = calculator( data )
            if res: 
                res = struct.pack( 'f', res )
                connection.send( res )
        else: 
            break


count : int = 0 
while True: 

    # Aguarda até alguma conexão ser solicitada 
    connection, ( IPClient, PortClient) = server.accept()
    count += 1
    
    # Inicia uma thread para rodar multi clientes 
    _thread.start_new_thread( multi_threaded_client, ( connection, ) )

    print( 'Connected {} with IP {} '.format( IPClient, PortClient ) )
    print('Thread Number: ' + str(count) )