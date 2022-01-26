"""
Tic Tac Toe Player
"""

import copy

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
    x, o = 0, 0
    for ar in board:
        for i in ar:
            if i == X:
                x = x+1
            elif i == O:
                o = o+1
    if x > o:
        return(O)
    else:
        return(X)



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, ar in enumerate(board):
        for j, a in enumerate(ar):
            if a == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    cop = copy.deepcopy(board)
    if(cop[action[0]][action[1]] == EMPTY):
        cop[action[0]][action[1]] = player(board)
    else:
        raise
    return cop



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        test = board[i][0]
        if (test == board[i][1]) and (test == board[i][2]):
            return test
        if (board[0][i] == board[1][i]) and (board[0][i] == board[2][i]):
            return board[0][i]
        if i == 0:
            if (test == board[1][1]) and (test == board[2][2]):
                return test
        if i == 2:
            if (test == board[1][1]) and (test == board[0][2]):
                return test

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for ar in board:
        for a in ar:
            if a == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    if win == O:
        return -1
    return 0



def max_value(board):
    if terminal(board):
        return utility(board)

    moves = actions(board)
    min = -2
    for move in moves:
        fake_board = result(board, move)
        val = min_value(fake_board)
        if val >= min:
            min = val
    return min


def min_value(board):
    if terminal(board):
        return utility(board)

    moves = actions(board)
    max = 2
    for move in moves:
        fake_board = result(board, move)
        val = max_value(fake_board)
        if val <= max:
            max = val
    return max


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    turn = player(board)
    moves = actions(board)
    if turn == X:
        max = -2
        for move in moves:
            val = min_value(result(board, move))
            if val == 1:
                return move
            else:
                if val > max:
                    max = val
                    the_move = move

    if turn == O:
        min = 2
        for move in moves:
            val = max_value(result(board, move))
            if val == -1:
                return move
            else:
                if val < min:
                    min = val
                    the_move = move

    return the_move
