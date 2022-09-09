from Pieces import Piece, Pawn, Rook, Knight, Bishop, Queen, King


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



def print_board( print_value = False ):
    string_row = '   '
    for c in collums_number:
        string_row += c+' '
    string_row +='\n'
    for r in range(len(row_letters)):
        string_row += row_letters[r]+'  ' 
        for c in range(len(collums_number)):
            if print_value:
                string_row += str(board[r][c].value) + ' '
            else:
                string_row += board[r][c].ascii_symbol + ' '
        string_row += '\n'
    print(string_row)



if __name__ == '__main__': 
    
    # Criar o tabuleiro em matriz e colocar as peças em cima 

    collums_number = [ '1', '2', '3', '4', '5', '6', '7', '8' ] 
    row_letters    = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]

    board = [ [ Piece( r, c, 'DEFAULT' ) for c in range(8) ] for r in range(8) ]

    put_pieces_on_the_board()
    print_board()

    print( board[7][0].move(5,0, board) )
    print_board()

    print( board[7][1].move(5,2, board ) )
    print_board()

    


