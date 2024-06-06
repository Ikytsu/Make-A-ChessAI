import chess.svg
import sys
import output_names
import os
import chess.engine
sys.path.insert(1, 'usef_ais')

if len(sys.argv) == 1:
    (print
    ("""-usei [against_ai_name]
    \n-usef [against_ai_name]
    \n-starter [true/false]
    \n-debug
    """
    )
    )
else:
    i = 1
    usei_used = False
    usef_used = False
    using_AI = ""
    starter_used = False
    using_starter = True
    debug = False


    while i < len(sys.argv):
        if sys.argv[i] == "-usei":

            if len(sys.argv) == i + 1:
                raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_nothingafter)

            elif not usei_used and not usef_used:
                usei_used = True
                using_AI = sys.argv[i + 1]
                i += 1
            else:
                raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_muchuse)

        elif sys.argv[i] == "-usef":

            if len(sys.argv) == i + 1:
                raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_nothingafter)

            elif not usei_used and not usef_used:
                usef_used = True
                using_AI = sys.argv[i + 1]
                i += 1
            else:
                raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_muchuse)

        elif sys.argv[i] == "-starter":

            if len(sys.argv) == i + 1:
                raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_nothingafter)

            elif not starter_used:
                starter_used = True
                if sys.argv[i + 1] == "true":
                    i += 1
                elif sys.argv[i + 1] == "false":
                    using_starter = False
                    i += 1
                else:
                    raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_unknown)
            else:
                raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_muchstarter)

        elif sys.argv[i] == "-debug":

            if not debug:
                debug = True

            else:
                raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_muchdebug)

        else:raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_unknown)
        i += 1

    if debug: print("Checking if there is an use of an ai..")

    if not usei_used and not usef_used:raise Exception(output_names.Arg_ERR, output_names.Specific_Arg_ERR_nouse)

    if debug: print("Checking if the choosen AI exists..")

    if usei_used:
            path = "usei_ais/" + using_AI
            if not os.path.exists(path): raise Exception(output_names.File_ERR, output_names.Specific_File_ERR_unexstitent)
            engine = chess.engine.SimpleEngine.popen_uci(path)

    elif usef_used:
            path = "usef_ais/" + using_AI + ".py"
            if not os.path.exists(path): raise Exception(output_names.File_ERR, output_names.Specific_File_ERR_unexstitent)

            print("You are going to execute unverified code, it can be potentially dangerous and it's highly recommended to verify the usef file")
            ask = input("Are you sure to proceed? [y/n]")
            if ask != "y":
                sys.exit("canceled training")
            else:
                module = __import__(using_AI)
                find_best_move = getattr(module, 'get_best_move')

    if not starter_used and debug:print("No defined starter, starting as white..")

    if debug:print("initializing the board..")
    board = chess.Board()
    i = 0
    if debug:print("starting to generate svg...")
    if debug: print("move", i)
    svg_board = chess.svg.board(board=board)
    f = open("output/" + str(i), "w")
    f.write(svg_board)
    f.close()
    while not board.is_checkmate() and not board.is_stalemate() and not board.is_insufficient_material() and not board.can_claim_threefold_repetition():
        i += 1
        if debug: print("move", i)
        if usef_used:
            if using_starter:
                result = get_best_move(board, 3, using_starter)
                if debug: print(result)
                board.push(result)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()
                i += 1
                if debug: print("move", i)
                result = find_best_move(board, 3, not using_starter)
                if debug: print(result)
                board.push(result)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()
            else:
                result = find_best_move(board, 3, not using_starter)
                if debug: print(result)
                board.push(result)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()
                i += 1
                if debug: print("move", i)
                result = get_best_move(board, 3, using_starter)
                if debug: print(result)
                board.push(result)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()

        if usei_used:
            if using_starter:
                result = get_best_move(board, 3, using_starter)
                print(result)
                board.push(result)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()
                i += 1
                if debug: print("move", i)
                result = engine.play(board, chess.engine.Limit(time=1))
                if debug: print(result)
                board.push(result.move)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()
            else:
                result = engine.play(board, chess.engine.Limit(time=1))
                if debug: print(result)
                board.push(result.move)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()
                i += 1
                if debug: print("move", i)
                result = get_best_move(board, 3, using_starter)
                if debug: print(result)
                board.push(result)
                svg_board = chess.svg.board(board=board)
                f = open("output/" + str(i), "w")
                f.write(svg_board)
                f.close()
    if debug: print("ended")
    if usei_used: engine.quit()
