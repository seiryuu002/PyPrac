# ____________________________TIC_TAC_TOE_GAME______________________________
# This is tic-tac-toe game, two players can play at a time and select where
# the want to put their respective marks 'O' or 'X'.  

# first function to display tic-tac-toe board on screen
import random

tic_tac = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(tic_tac):
    print('\n'*2)
    print(f"  {tic_tac[7]} |  {tic_tac[8]}  | {tic_tac[9]} ")
    print("----|-----|----")
    print(f"  {tic_tac[4]} |  {tic_tac[5]}  | {tic_tac[6]} ")
    print("----|-----|----")
    print(f"  {tic_tac[1]} |  {tic_tac[2]}  | {tic_tac[3]} ")
    print('\n'*2)


def user_choice():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    return ((board[7] == board[8] == board[9] == mark) or  # across the top
            # across the middle
            (board[4] == board[5] == board[6] == mark) or
            # across the bottom
            (board[1] == board[2] == board[3] == mark) or
            # down the middle
            (board[7] == board[4] == board[1] == mark) or
            # down the middle
            (board[8] == board[5] == board[2] == mark) or
            # down the right side
            (board[9] == board[6] == board[3] == mark) or
            # diagonal
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))  # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board, turn):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(f'Choose your next position {turn}: (1-9) '))

    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = user_choice()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
