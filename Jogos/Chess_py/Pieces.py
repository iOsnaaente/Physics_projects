# Pieces in ASCII formact 
pieces_dict = {
            'WHITE' : { 'pawn' : "♙", 'rook' : "♖", 'knight' : "♘", 'bishop' : "♗", 'king' : "♔", 'queen' : "♕" },
            'BLACK' : { 'pawn' : "♟", 'rook' : "♜", 'knight' : "♞", 'bishop' : "♝", 'king' : "♚", 'queen' : "♛" },
            'EMPTY' : { 'empty': " " }
            }

# Class default to create the especifics pieces like pawns and rocks 
class Piece: 

    ascii_symbol = ' '
    color = ''
    value = 0 
    name = ''

    pos = [-1, -1]
    

    def __init__(self, r : int, c : int, color : str ):
        self.color = color.upper()
        self.pos = [ r, c ]
        self.set_value( 0 ) 


    # Use to move a piece to a new position in the board 
    # if \return equal to False, the piece can't move
    # if \return equal to True, the piece was moved 
    def move(self, row_goal : int, collum_goal : int, board : list) -> bool: 
        if self.value == 0:
            print('No piece available on here to move...')
            return False

        row    = self.pos[0]
        collum = self.pos[1]

        moves = self.moves_available( board ) 
        goal = [ row_goal, collum_goal ]

        for move in moves: 
            if goal[0] == move[0] and goal[1] == move[1] : 
                # If the goal position is available, move the pawn to the board goal position 
                board[row][collum], board[row_goal][collum_goal] = Piece(row, collum, 'DEFAULT'), board[row][collum]
                if self.first_move:
                    self.first_move = False 
                return True 

        return False
    

    # befero to move, verify if the pos_goal is available 
    def piece_on_the_position(self, pos : list, board) -> object:
        # Melhor que verificar se x_goal e y_goal estão nos limites 
        # É usar um Try/except pois são raras as vezes que pode ocorrer 
        try:
            return board[ pos[0] ][ pos[1] ] 
        except: 
            return "Posição inválida" 

            
    # return a list with all moviments available to move the piece 
    def moves_available(self, board) -> list :  
        print( 'No piece available to check the moves available') 
    

    # After the init_especific_piece was called, set the value 
    def set_value(self, value : int ):
        if self.color == 'WHITE':
            self.value = value *  1
        elif self.color == 'BLACK':
            self.value = value * -1
        else:
            self.ascii_symbol = pieces_dict['EMPTY']['empty']
            self.value = 0 




# ♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟ #
# ♙♟                                                       ♙♟ #
# ♙♟                       PAWN                            ♙♟ #
# ♙♟                                                       ♙♟ #
# ♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟♙♟ #

class Pawn( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['pawn'] 
        self.name = 'Pawn'
        self.set_value( 1 )
        self.first_move = True 
    
    def moves_available(self, board):
        r = self.pos[0]
        c = self.pos[1]

        if self.color == 'WHITE':
            pos_to_run    = [ [r+1, c], [r+2, c], [r+1, c-1], [r+1, c+1] ]
        elif self.color == 'BLACK':
            pos_to_run    = [ [r-1, c], [r-2, c], [r-1, c-1], [r-1, c+1] ]
        available_pos = []

        piece_ahead = self.piece_on_the_position( pos_to_run[0], board )
        if piece_ahead.value == 0:
            try:
                available_pos.append( pos_to_run[0] )
                if self.first_move:
                    piece_ahead = self.piece_on_the_position ( pos_to_run[1], board )
                    if piece_ahead.value == 0:
                        available_pos.append( pos_to_run[1] )
            except:
                pass 

        for pos in pos_to_run[-2: ]:
            try:
                piece_ahead = self.piece_on_the_position( pos, board )
                if piece_ahead.value*self.value < 0:
                    available_pos.append( pos )
            except:
                continue 

        return available_pos 



       
        



# ♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜ #
# ♖♜                                                       ♖♜ #
# ♖♜                        ROOK                           ♖♜ #
# ♖♜                                                       ♖♜ #
# ♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜♖♜ # 

class Rook( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['rook'] 
        self.name = 'Rook'        
        self.set_value( 5 )
        self.first_move = True 
        
    def moves_available(self, board):
        r = self.pos[0]
        c = self.pos[1]

        available_pos = []

        # Anda para Cima nas linhas 
        for up_row in range(1, 8):
            try:
                piece_ahead = self.piece_on_the_position( r + up_row, c ) 
                if piece_ahead.value == 0 or piece_ahead.value * self.value < 0: 
                    available_pos.append( r + up_row, c )
                else: 
                    break
            except:
                break

        # Anda para Baixo nas linhas  
        for down_row in range(1, 8):
            try:
                piece_ahead = self.piece_on_the_position( r - up_row, c ) 
                if piece_ahead.value == 0 or piece_ahead.value * self.value < 0: 
                    available_pos.append( r - up_row, c )
                else: 
                    break
            except:
                break

        # Anda para a Direita nas colunas 
        for up_collum in range(1, 8):
            try: 
                piece_ahead = self.piece_on_the_position( r, c + up_collum )
                if piece_ahead.value == 0 or piece_ahead.value * self.value < 0:
                    available_pos.append( r, c + up_collum )
                else:
                    break 
            except:
                break 

        # Anda para a Esquerda nas colunas 
        for up_collum in range(1, 8):
            try:
                piece_ahead = self.piece_on_the_position( r, c + up_collum )
                if piece_ahead.value == 0 or piece_ahead.value * self.value < 0:
                    available_pos.append( r, c + up_collum )
                else:
                    break 
            except: 
                break



# ♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞ # 
# ♘♞                                                       ♘♞ #
# ♘♞                      KNIGHT                           ♘♞ #
# ♘♞                                                       ♘♞ #
# ♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞♘♞ #

class Knight( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['knight'] 
        self.name = 'Knight'        
        self.set_value( 3 )
        self.first_move = True 
        
    def moves_available(self, board : list) -> list :
        
        r = self.pos[0]
        c = self.pos[1]

        pos_to_run    = [ [r+2, c+1], [r+2, c-1], [r-2, c+1], [r-2, c-1],
                          [r+1, c+2], [r+1, c-2], [r-1, c+2], [r-1, c-2]  ]
        
        available_pos = []

        for pos in pos_to_run:
            piece_ahead = self.piece_on_the_position( pos, board )
            if piece_ahead.value * self.value < 0 or piece_ahead.value == 0:
                available_pos.append( pos )





# ♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝ # 
# ♗♝                                                       ♗♝ #
# ♗♝                      BISHOP                           ♗♝ #
# ♗♝                                                       ♗♝ #
# ♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝♗♝ #

class Bishop( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['bishop'] 
        self.name = 'Bishop'
        
    def move(self, x_goal, y_goal):
        pass 







# ♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛ #
# ♕♛                                                   ♕♛ #
# ♕♛                        QUEEN                      ♕♛ #
# ♕♛                                                   ♕♛ #
# ♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛♕♛ #
  
class Queen( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['queen'] 
        self.name = 'queen'
        
    def move(self, x_goal, y_goal):
        pass 




# ♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚ #
# ♔♚                                                       ♔♚ #
# ♔♚                      KING                             ♔♚ #
# ♔♚                                                       ♔♚ #
# ♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚♔♚ #

class King( Piece ):

    def __init__(self, x : int, y : int, color : str ):
        super().__init__(x, y, color)
        self.ascii_symbol = pieces_dict[self.color]['king'] 
        self.name = 'King'
        
    def move(self, x_goal, y_goal):
        pass 