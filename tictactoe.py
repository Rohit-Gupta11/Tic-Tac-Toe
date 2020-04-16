#-------------------------------------Global variable------------------------------------------------------------------
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

current_player = ""

game_is_running = True

winner = None
#-----------------------------------play game function--------------------------------------------------------------------------
def play_game():
    display_board()
    select_first_player()
    while game_is_running:
        handle_turn()
        flip_player()
        display_board()
        check_for_result()
    

    if winner == "X" or winner =="O":
        print("the winner is " + winner)
    elif winner == None:
        print("It's tie")





#---------------------------------game functions-----------------------------------------------------------------------
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2]+ "            1|2|3")
    print(board[3] + "|" + board[4] + "|" + board[5]+ "            4|5|6")
    print(board[6] + "|" + board[7] + "|" + board[8]+ "            7|8|9")
    return

def select_first_player():
    global current_player , game_is_running
    current_player = input("Choose X or O for first player : ")
    if current_player == "X" or current_player == "O":
        print("The first player is " + current_player)
    else:
        game_is_running = False
        print("Unknown entry\nRestsart game")
    return

def handle_turn():
    position = input("Choose position from 1-9 : ")
    position = int(position) - 1
    if board[position] == "-":
        board[position] = current_player
    else:
        print("Already acquired!\nTry another")
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    print("It's your turn " + current_player)
    return

def check_for_result():
    check_for_win()
    check_for_tie()

def check_for_win():
    global winner
    row_winner = check_rows()
    col_winner = check_columns()
    diag_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None

def check_rows():
    global winner,game_is_running
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_is_running = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    global winner,game_is_running
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_is_running = False
    if col_1:
        return board[0]
    elif col_2:
        return board[3]
    elif col_3:
        return board[6]
    else:
        return None

def check_diagonals():
    global winner,game_is_running
    diag_1 = board[0] == board[1] == board[2] != "-"
    diag_2 = board[3] == board[4] == board[5] != "-"
    if diag_1 or diag_2:
        game_is_running = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[4]
    else:
        return None

def check_for_tie():
    global game_is_running
    if "-" not in board:
        game_is_running = False
        return True
    else:
        return False



    
#--------------------------------Initializing game---------------------------------------------------------------------
play_game()