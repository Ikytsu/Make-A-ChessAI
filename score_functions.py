import chess

def piece_value(board, white:bool):
    if white:
        white_material = board.occupied_co[chess.WHITE]
        white_pawns = chess.popcount(white_material & board.pawns)
        white_knights = chess.popcount(white_material & board.knights)
        white_bishops = chess.popcount(white_material & board.bishops)
        white_rooks = chess.popcount(white_material & board.rooks)
        white_queens = chess.popcount(white_material & board.queens)
        score = white_pawns + white_pawns * 3 + white_pawns * 3 + white_pawns * 5 + white_pawns * 8
    else:
        black_material = board.occupied_co[chess.BLACK]
        black_pawns = chess.popcount(black_material & board.pawns)
        black_knights = chess.popcount(black_material & board.knights)
        black_bishops = chess.popcount(black_material & board.bishops)
        black_rooks = chess.popcount(black_material & board.rooks)
        black_queens = chess.popcount(black_material & board.queens)
        score = black_pawns - black_knights * 3 - black_bishops * 3 - black_rooks * 5 - black_rooks * 8
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

