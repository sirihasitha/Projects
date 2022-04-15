"""
Tic Tac Toe Player
"""

import math,copy

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
    y = [item for sublst in board for item in sublst]
    #if y.count(X) == 0 and y.count(Y) == 0:
    	#return X
    if y.count(X) > y.count(O):
    	return O
    else:
    	return X
    #raise NotImplementedError
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    y = [item for sublst in board for item in sublst]
    flat_list =[(i,j) for i in range(0,3) for j in range(0,3) if board[i][j] == EMPTY] 
    
    return flat_list

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardc = copy.deepcopy(board)
    x, y = action
    if board[x][y] != EMPTY:
        raise IndexError
    else:

        play = player(board)
        boardc[x][y] = play
    return boardc
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for sub in board:
    	if all([ele == sub[0] for ele in sub]):
    		return sub[0]
    		
    rez = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] 
    for sub in rez:
    	if all([ele == sub[0] for ele in sub]):
    		return sub[0]
	
    #print(rez)		
    res =[board[i][j] for i in range(0,3) for j in range(0,3) if i == j]
    if all([ele == res[0] for ele in res]):
    		return res[0]
    		
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[1][1]
        
    l1 = [(i,j) for i in range(0,3) for j in range(0,3) if board[i][j] != EMPTY]
    if len(l1) == 9:
        return "Draw"
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) == X or winner(board) == O or winner(board) == "Draw"
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        else:
            return 0
    #raise NotImplementedError
def maxi(board):
	if terminal(board):
		return utility(board)
	else:
		best = float('-inf')
		for action in actions(board):
			res = mini(result(board, action))                      # v = MAX(v, MIN-VALUE(RESULT(state, action)))
			best = max(best, res)
		return best
def mini(board):
	if terminal(board):
		return utility(board)
	else:
		best = float('inf')
		for action in actions(board):
			res = maxi(result(board, action))                      # v = MAX(v, MIN-VALUE(RESULT(state, action)))
			best = min(best, res)
		return best

def minimax(board):
    play = player(board)
    if play == X:
        v = float('-inf')
        for action in actions(board):
            res = mini(result(board, action))
            if res > v:
                v = res
                best = action
    else:
        v = float('inf')
        for action in actions(board):
            res = maxi(result(board, action))
            if res < v:
                v = res
                best = action
    return best
