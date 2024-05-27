import chess

def piece_value(board, white:bool):
    if white:
        white_material = board.occupied_co[chess.WHITE]
        white_pawns = chess.popcount(white_material & board.pawns)
        white_knights = chess.popcount(white_material & board.knights)
        white_bishops = chess.popcount(white_material & board.bishops)
        white_rooks = chess.popcount(white_material & board.rooks)
        white_queens = chess.popcount(white_material & board.queens)
        score = white_pawns * 50 + white_knights * 150 + white_bishops * 150 + white_rooks * 300 + white_queens * 1000
    else:
        black_material = board.occupied_co[chess.BLACK]
        black_pawns = chess.popcount(black_material & board.pawns)
        black_knights = chess.popcount(black_material & board.knights)
        black_bishops = chess.popcount(black_material & board.bishops)
        black_rooks = chess.popcount(black_material & board.rooks)
        black_queens = chess.popcount(black_material & board.queens)
        score = black_pawns * 50 - black_knights * 150 - black_bishops * 150 - black_rooks * 300 - black_queens * 1000
    return score

def developpement_value(board, white:bool):
    pass

def pawnstructure_value(board, white:bool):
    pass

def kingsafety_value(board, white:bool):
    pass

def centercontrol_value(board, white:bool):
    pass

def piece_mobility_value(board, white:bool):
    pass

def pawn_initiative_value(board, white:bool):
    pass

