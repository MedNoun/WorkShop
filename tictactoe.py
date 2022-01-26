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
    
    return


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    return
    



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return



def max_value(board):
    return


def min_value(board):
    
    return

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return
