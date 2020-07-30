#
game_still_going = True
current_player = 'X'
#################board####################
board = ['-','-','-','-','-','-','-','-','-',]
##############display board#################
def display_board():
    print(' |' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print(' |' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print(' |' + board[6] + '|' + board[7] + '|' + board[8] + '|')

################play game####################
def play_game():
    global game_still_going
    global current_player

    display_board()
    while game_still_going:
        player_turn(current_player)
        check_if_win()
        flip_player()

def player_turn(player):
    global current_player
    position = input('{} choose position from 1-9:'.format(player))
    #checking input corectness
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Wrong position! {} choose position from 1-9:'.format(player))
    while '-' not in board[(int(position)-1)]:
        position = input('Wrong position! {} choose position from 1-9:'.format(player))

    position = int(position) - 1
    board[position] = current_player
    display_board()


def check_if_win():
    check_for_winner()
    check_if_tie()


# Check win
def check_for_winner():
    row_winner = check_rows()
    column_winner = check_columns()
    diag_winner = check_diagonals()
    if row_winner == 'X' or row_winner == 'O':
        print(str(row_winner) + ' won.')
    elif column_winner == 'X' or column_winner == 'O':
        print(str(column_winner) + ' won.')
    elif diag_winner == 'X' or diag_winner=='O':
        print(str(diag_winner) + ' won.')



############check rows###################
def check_rows():
    global game_still_going
    row_1 = board[0]==board[1]==board[2]!= "-"
    row_2 = board[3]==board[4]==board[5]!= "-"
    row_3 = board[6]==board[7]==board[8]!= "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    elif row_3:
        return board[6]

###########check columns#################
def check_columns():
    global game_still_going
    column_1=board[0]==board[3]==board[6]!='-'
    column_2=board[1]==board[4]==board[7]!='-'
    column_3=board[2]==board[5]==board[8]!='-'
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    elif column_3:
        return board[2]
###########check diagonals##############
def check_diagonals():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[2] == board[4] == board[6] != '-'
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
#################check tie###################
def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
        print('Tie!')
################flip player##################
def flip_player():
    global current_player
    if current_player == 'O':
        current_player = 'X'
    elif current_player == 'X':
        current_player = 'O'
    return




play_game()


