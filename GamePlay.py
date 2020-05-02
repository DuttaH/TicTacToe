from GameCourt import *

msg = ['Player ',
       'Game Draw',
       'Winner : ',
       'Press any key to continue...',
       'ERROR# Cell already occupied',
       'ERROR# Invalid input',
       'Do you want to save the game? (Y/N) ',
       'Your Game has been saved. Press any key to quit...'
       ]


def save_game(ct):
    input(msg[7])


def game_status(ct):
    # Check any column, row or diagonals have save values or not
    # Check rows
    if ct['7'] == ct['8']== ct['9'] != ' ':
        return ct['7']
    elif ct['4'] == ct['5'] == ct['6'] != ' ':
        return ct['4']
    elif ct['1'] == ct['2'] == ct['3'] != ' ':
        return ct['1']
    # Check columns
    elif ct['7'] == ct['4'] == ct['1'] != ' ':
        return ct['7']
    elif ct['8'] == ct['5'] == ct['2'] != ' ':
        return ct['8']
    elif ct['9'] == ct['6'] == ct['3'] != ' ':
        return ct['9']
    # Check diagonals
    elif ct['7'] == ct['5'] == ct['3'] != ' ':
        return ct['7']
    elif ct['9'] == ct['5'] == ct['1'] != ' ':
        return ct['9']
    # If there is no match, check for empty cell. If empty cell is available then continue else game draw
    elif ' ' in ct.values():
        return 'C'
    else:
        return 'D'


def new_game():
    # Initialize new court
    ct = {'7': ' ', '8': ' ', '9': ' ',
          '4': ' ', '5': ' ', '6': ' ',
          '1': ' ', '2': ' ', '3': ' ',
          }
    print_court(ct, 9)
    # Initialize game variables
    status = 'C'
    draw = 'X'
    move = ' '
    # Game is being played within loop. Loop will run until winner is decided / drawn or back / exit input received
    while status == 'C':
        # Get user input
        move = input(msg[0] + draw + ':').upper()
        # Check whether user want to back from game
        if move == 'B':
            return
        # Check whether user want to quit the game
        elif move == 'Q':
            sv_game = input(msg[6]).upper()
            if move == 'Y':
                save_game(ct)
            return
        # Validate and record the move
        elif move in ct.keys():
            if ct[move] == ' ':
                ct[move] = draw
            else:
                print(msg[4])
                continue
        else:
            print(msg[5])
            continue
        print_court(ct, 9)
        # Swap the player
        if draw == 'X':
            draw = 'O'
        elif draw == 'O':
            draw = 'X'
        # Get the ame status
        status = game_status(ct)
    # print result of the game
    if status == 'D':
        print(msg[1])
    else:
        print(msg[2], status)
    input(msg[3])
    return
