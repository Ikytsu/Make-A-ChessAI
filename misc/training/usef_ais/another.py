import random
import chess

def get_best_move(board):
    ListOfmove = list(board.legal_moves)
    randomChoice = random.choice(ListOfmove)
    return str(randomChoice)