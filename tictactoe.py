"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xcount += 1
            elif board[i][j] == O:
                Ocount += 1

    if Xcount > Ocount:
        NextPlayer = O
    else:
        NextPlayer = X

    return NextPlayer                            
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleactions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleactions.add((i,j))
        
    return possibleactions            



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #Board is the deepcopy of the original board
    Board = copy.deepcopy(board)

    if  Board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action")

    #updating the board with action
    Board[action[0]][action[1]] = player(Board)

    return Board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == X and board [1][1] == X and board [2][2] == X:
        return X
    elif board[0][2] == X and board [1][1] == X and board[2][0] == X:
        return X     
    elif board[0][0] == O and board [1][1] == O and board [2][2] == O:
        return O
    elif board[0][2] == O and board [1][1] == O and board[2][0] == O:
        return O     

    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[0][i] == X and board[1][i] == X and board [2][i] == X:
            return X    
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O
        elif board[0][i] == O and board[1][i] == O and board [2][i] == O:
            return O   

    return None                     



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True            


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    
    elif winner(board) == O:
        return -1

    return 0        


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None

    if player(board) == X:
        optimal_move =  Max_value(board)

    elif player(board) == O:
        optimal_move = Min_value(board)

    return optimal_move[1]    


def Max_value(board):

    v = -math.inf
  

    for action in actions(board):
        
        #if winning state of X is encountered immediately return that move

        if terminal(result(board,action)) == True:
            v = utility(result(board,action))
            next_action = action
            print(v, next_action)
            return(v, next_action)
           
        else:    
            #Breaking down max(v, Min_value(result(board,action)))   
            
            pos = Min_value(result(board,action))[0]
            

            #Maximum value of Min_value, next_action is the action whichgives the highest value of v
            if pos > v:
                v = pos
                next_action = action
            

    print(v, next_action)
    return (v, next_action)


def Min_value(board):

    v = math.inf


    for action in actions(board):

        #if winning state of O is encountered immediately return that move 
        
        
        if terminal(result(board,action)) == True:
            v = utility(result(board,action))
            next_action = action
            print(v, next_action)
            return(v, next_action)
           

        else:   
            #breaking down min(v,Max_value(result(board,action)))
            pos =  Max_value(result(board,action))[0]
            

            #minimum value of max-value, next_action is the action which gives lowest value of v
            if pos < v:
                v = pos
                next_action = action
                

    #(Min_value[0],Min_value[1])
    
    return (v,next_action)        

