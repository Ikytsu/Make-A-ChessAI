#AI here is maximizing and the opponnent minimize!

import chess
from score_functions import *

def evaluate(board, white:bool):
    score = 0
    maximizing = white
    minimizing = not white

    score += piece_value(board, maximizing)
    score -= piece_value(board, minimizing)

    """score += developpement_value(board, maximizing)
    score -= developpement_value(board, minimizing)

    score += pawnstructure_value(board, maximizing)
    score -= pawnstructure_value(board, minimizing)

    score += kingsafety_value(board, maximizing)
    score -= kingsafety_value(board, minimizing)

    score += centercontrol_value(board, maximizing)
    score -= centercontrol_value(board, minimizing)

    score += piece_mobility_value(board, maximizing)
    score -= piece_mobility_value(board, minimizing)

    score += pawn_initiative_value(board, maximizing)
    score -= pawn_initiative_value(board, minimizing)"""

    return score


def minmax(board, maximizing_player, depth, alpha, beta, white:bool):
    if board.is_checkmate():
        return float('-inf') if maximizing_player else float("inf")
    if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition() or depth == 0:
        return evaluate(board, white)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board_for_minmax = board.copy()
            board_for_minmax.push(move)
            eval = minmax(board_for_minmax, False, depth - 1, alpha, beta, white)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board_for_minmax = board.copy()
            board_for_minmax.push(move)
            eval = minmax(board_for_minmax, True, depth - 1, alpha, beta, white)
            min_eval = min(min_eval, eval)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board, depth, white:bool):
    best_eval = float('-inf')
    for move in board.legal_moves:
        board_for_minmax = board.copy()
        board_for_minmax.push(move)
        eval = minmax(board_for_minmax, False, depth - 1, float('-inf'), float('inf'), white)
        if eval >= best_eval:
            bestmove = move
            best_eval = eval
    return bestmove


