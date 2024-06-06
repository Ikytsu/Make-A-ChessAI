#import
import random
import matplotlib.pyplot as plt
from main import *
sys.path.insert(1, 'path to parent directory (Make-A-ChessAI)') ; from ai import *

n = 0
Starter = ""
white = None
defined_depth = 3

def Update(ax, LastPlayer):
    svg_board = chess.svg.board(board=board)

    png_board = cairosvg.svg2png(bytestring=svg_board)

    image_data = io.BytesIO(png_board)

    # setup de l'image pour la mettre en page plus tard
    image_box = OffsetImage(plt.imread(image_data), zoom=0.8)



    ABb = AnnotationBbox(image_box, (0.5, 0.5), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
    ax.add_artist(ABb)

    plt.draw()
    DisplayAvalaibleMove(ax, LastPlayer)

def Move(c):
    Reussi = False
    try:
        board.push_san(c)
        Reussi = True
    except:
        plt.title("Illegal move")
        plt.draw()
    return Reussi

def DisplayAvalaibleMove(ax, LastPlayer):
    if LastPlayer == False:
        StrTitle = "Possible moves: "
        for index, move in enumerate(board.legal_moves):
            if index > 0:
                StrTitle += ", "
            StrTitle += str(move)
        plt.title(StrTitle)
        plt.draw()
    elif LastPlayer == True:
        plt.title("AI turn, thinking...")
        plt.draw()
    else:
        plt.title("Fatal error")
        plt.draw()

def SubmitText(text, ax, textbox):
    global n
    global gameover
    global Starter
    global white

    gameover = (board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition())
    textbox.set_val("")
    if not gameover and Starter != "":

        if Starter == "Debug":
            if n%2 == 0:
                if Move(text) == True:
                    n += 1
                    Update(ax, False)
            else:
                if Move(text) == True:
                    n += 1
                    Update(ax, False)

        elif Starter == "Player":
            if n%2 == 0:
                if Move(text) == True:
                    n += 1
                    C = get_best_move(board, defined_depth, white)
                    Move(str(C))
                    n += 1
                    Update(ax, False)

        elif Starter == "AI":
            if n%2 != 0:
                if Move(text) == True:
                    n += 1
                    C = get_best_move(board, defined_depth, white)
                    Move(str(C))
                    n += 1
                    Update(ax, False)

    #Choix de celui qui commence la partie
    elif Starter == "":

        if text == "Player":
            Starter = "Player"
            white = False
            DisplayAvalaibleMove(ax, False)

        elif text == "AI":
            Starter = "AI"
            white = True
            DisplayAvalaibleMove(ax, True)
            C = get_best_move(board, defined_depth, white)
            Move(str(C))
            n += 1
            Update(ax, False)

        elif text == "Debug":
            Starter = "Debug"
            DisplayAvalaibleMove(ax, False)

        else:
            plt.title("Put a correct choice")
            plt.draw()
