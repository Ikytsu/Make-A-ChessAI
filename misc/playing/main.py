import chess
import os
import random
import chess.svg
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import cairosvg
import io
import matplotlib
import time
import threading
import sys
from matplotlib.widgets import TextBox

board = chess.Board()

gameover = (board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition() or board.halfmove_clock or board.can_claim_fifty_moves())

if __name__ == "__main__":
    import functions

    svg_board = chess.svg.board(board=board)

    png_board = cairosvg.svg2png(bytestring=svg_board)

    image_data = io.BytesIO(png_board)

    fig, ax = plt.subplots()

    image_box = OffsetImage(plt.imread(image_data), zoom=0.8)

    ABb = AnnotationBbox(image_box, (0.5, 0.5), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
    ax.add_artist(ABb)

    axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
    text_box = TextBox(axbox, "Evaluate", textalignment="center")
    text_box.on_submit(lambda text: functions.SubmitText(text, ax, text_box))

    plt.title("Choose who starts, AI, Player or Debug (player against player)")

    plt.show()