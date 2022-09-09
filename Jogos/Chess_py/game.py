from Pieces import * 
import pygame


def verify_piece_on_the_board( pos : list) -> Piece : 
    global board 

    x = pos[0]//100 
    y = pos[1]//100

    for r in range(8):
        for c in range(8):
            if board[r][c].pos == [ x, y]:
                print( board[r][c].ascii_symbol, x, y ) 



def put_pieces_on_the_board():
    global board 
    # Define the real-pieces order  
    pieces = [ Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook ]

    # Put the real-pieces on the board 
    board[0] = [ piece(0, n, "WHITE") for n, piece in enumerate(pieces) ]
    board[7] = [ piece(7, n, "BLACK") for n, piece in enumerate(pieces) ]

    # Put the pawns 
    board[1] = [ Pawn(1, c, "WHITE") for c in range( len( collums_number) ) ]
    board[6] = [ Pawn(6, c, "BLACK") for c in range( len( collums_number) ) ]

    draw_tiles() 


def draw_tiles():
    global screen 
    global board
    
    fonte = pygame.font.SysFont( systemFont, 30 )
    
    for r in range(8):
        for c in range(8):

            color = (r + c) % 2  

            surface = pygame.Surface((98,98))
            surface.fill( [150,255,150] if color else [255,255,255] )
            

            symbol = board[r][c].name 

            text = fonte.render(symbol, 2, (0,0,0) )
            surface.blit( text, [15,35] )

            border = pygame.Surface( (100,100), 0)
            border.fill((200,150,100))

            border.blit(surface, (0,0))
            screen.blit( border, [r*100, c*100 ] )



screen_dimensions = [800, 800]

collums_number = [ '1', '2', '3', '4', '5', '6', '7', '8' ] 
row_letters    = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]

# Criar o tabuleiro em matriz e colocar as peças em cima 
board = [ [ Piece( r, c, 'DEFAULT' ) for c in range(8) ] for r in range(8) ]



# INICIANDO PROCESSO NO PYGAME
pygame.init()

pygame.font.init()
systemFont = pygame.font.get_default_font()

screen = pygame.display.set_mode( screen_dimensions )

pygame.display.set_caption("Chess Game - movimentation test")
pygame.display.set_icon( pygame.image.load("D:\Desktop\git\chess_train\Chess_py\knight_vector.png") ) 

clock = pygame.time.Clock()

put_pieces_on_the_board()

while True:

    # COLORIR O PLANO DE FUNDO COM A COR CINZA
    screen.fill( [255,255,255] )

    # BUSCA EVENTOS DENTRO DO PYGAME 
    for event in pygame.event.get():
        # SE O BOTÃO DE FECHAR FOR PRESSIONADO
        if event.type == pygame.QUIT:
            pygame.quit()

        # SE UMA TECLA FOR PRESSIONADO 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        # VERIFICA O MODO DO PROCESSO ATIVO
        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            verify_piece_on_the_board(coords)
            

    draw_tiles()



    pygame.display.update()
    clock.tick(60)