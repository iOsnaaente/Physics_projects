# Importações
import random

MAX_VALUE = 30
IDEAL_VALUE = 20 
NUM_JOGADAS = 0 
SCORE = 0 

# Tabuleiro NxM 
def build_table( X : int, Y : int ) -> list:
    return [ [ 0 for _ in range( Y ) ] for _ in range( X ) ]

# Movimentos para a direita soma
def move_right( TABLE : list ) -> list :
    global NUM_JOGADAS 
    NEW_TABLE = []
    for row in TABLE:
        flagSUM = True
        SUM = 0 
        ROW = [] 
        for value in row:
            if value != 0 and flagSUM: 
                flagSUM = False 
                SUM = value 
                ROW.append( 0 )
            elif value != 0 and not flagSUM:
                ROW.append( SUM + value )
                SUM = 0 
                flagSUM = True 
            else: 
                ROW.append(0)
        if flagSUM is False:
            ROW[-1] = SUM 
        NEW_TABLE.append( ROW )
    NUM_JOGADAS += 1 
    return NEW_TABLE

# Movimentos para a Esquerda subtrai 
def move_left( TABLE : list ) -> list:
    global NUM_JOGADAS 
    NEW_TABLE = []
    for row in TABLE:
        flagSUM = True
        SUM = 0 
        ROW = [] 
        for value in row[::-1]:
            if value != 0 and flagSUM: 
                flagSUM = False 
                SUM = value 
                ROW.append( 0 )
            elif value != 0 and not flagSUM:
                ROW.append( value - SUM )
                SUM = 0 
                flagSUM = True 
            else: 
                ROW.append(0)
        if flagSUM is False:
            ROW[-1] = SUM 
        NEW_TABLE.append( ROW[::-1] )
    NUM_JOGADAS += 1 
    return NEW_TABLE

# Movimentos para cima subtrai 
def move_up( TABLE : list ) -> list :
    global NUM_JOGADAS
    NEW_TABLE = list(map(list, zip(*TABLE))) 
    NEW_TABLE = move_left( NEW_TABLE )
    NEW_TABLE = list( map(list, zip(*NEW_TABLE)))
    NUM_JOGADAS += 1 
    return NEW_TABLE
    
# Movimentos para Baixo soma
def move_down( TABLE : list ) -> list:
    global NUM_JOGADAS
    NEW_TABLE = list( map( list, zip( *TABLE ) ) ) 
    NEW_TABLE = move_right( NEW_TABLE )
    NEW_TABLE = list( map(list, zip(*NEW_TABLE)))
    NUM_JOGADAS += 1 
    return NEW_TABLE

# Se alguma caixa alcançar o valor Twenty ela resulta em pontos 
def check_twenty( TABLE : list ):
    global SCORE, NUM_JOGADAS
    NEW_TABLE = TABLE 
    for row in range(len(TABLE)):
        for collum in range(len(TABLE[0])):
            if abs(TABLE[row][collum]) == IDEAL_VALUE :
                NEW_TABLE[row][collum] = 0 
                SCORE += ( IDEAL_VALUE + IDEAL_VALUE*10**(-NUM_JOGADAS/100) ) / 2
    return NEW_TABLE


# Se alguma caixa ultrapassar o valor de twenty five ela subtrai pontos 
def check_twenty_five( TABLE : list ) -> list :
    global SCORE, NUM_JOGADAS 
    NEW_TABLE = TABLE 
    for row in range(len(TABLE)):
        for collum in range(len(TABLE[0])):
            if abs(TABLE[row][collum]) >= MAX_VALUE*0.8:
                #if TABLE[row][collum] < 0:  NEW_TABLE[row][collum] += MAX_VALUE 
                #else:                       NEW_TABLE[row][collum] -= MAX_VALUE
                SCORE -= ( MAX_VALUE + MAX_VALUE*10**(-NUM_JOGADAS/100) ) / 2 
    return NEW_TABLE


# Verificar se o tabuleiro esta completamente preenchido
def check_end_game( TABLE : list ) -> bool: 
    flagEndGame = True 
    for row in TABLE:
        for collum in row:
            if collum >= MAX_VALUE: return True 
            elif collum == 0:       flagEndGame = False 
    if flagEndGame: return True 
    else:           return False

# Uma caixa é Spawnada por turno 
def spaw_new_turn( TABLE : list, turns : int = 1 ) -> list:
    for _ in range(turns):
        while True:
            X, Y = random.randint( 0, len(TABLE)-1 ), random.randint( 0, len(TABLE[0])-1 )
            if TABLE[X][Y] == 0:
                TABLE[X][Y] = random.randint( 0, 10 )
                break
    return TABLE

# Função para printar o tabuleiro na tela 
def print_game( TABLE : list ) -> None:
    global SCORE
    print( 'SCORE: %f' %SCORE )
    for x in TABLE:
        for y in x: 
            print( '%3i' %y , end = ' ' )
        print(' ')

# Iniciar o jogo e regras 
def init_game() -> None:
    TABLE = build_table( 4, 4 )
    TABLE = spaw_new_turn( TABLE, 4 )
    print_game( TABLE )
    while True:
        moves = input( 'Jogo: ' )
        for move in moves:
            if   move == 'a':   TABLE = move_left( TABLE )
            elif move == 's':   TABLE = move_down( TABLE )
            elif move == 'd':   TABLE = move_right( TABLE )
            elif move == 'w':   TABLE = move_up( TABLE )
            else:               continue

        TABLE = check_twenty( TABLE )
        TABLE = check_twenty_five( TABLE )
        if check_end_game( TABLE ):
            break
        TABLE = spaw_new_turn( TABLE, 2)
        print_game( TABLE )
    print( "Fim de jogo. Pontuação: %f " %SCORE)


#init_game()