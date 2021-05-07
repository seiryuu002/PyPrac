tic_tac = [0, 1, 2]
game_on = True
def display_game(tic_tac):
    print("here is the current list")
    print(tic_tac)

def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input("pick a position (0, 1, 2): ")

        if choice not in ['0', '1', '2']:
            print("sorry out of range choice please choose a position from (0, 1, 2)")

    return int(choice)

def replacemnt_choice(tic_tac, position):

    user_placement = input("Type a string to replace at position: ")
    tic_tac[position] = user_placement
    return tic_tac


def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input("keep Playing? (Y or N): ")
        if choice not in ['Y', 'N', 'y', 'n']:
            print("sorry invalid choice please choose Y or N")

    if choice == 'Y' or choice == 'y':
        return True
    else:
        return False

while game_on:
    display_game(tic_tac)
    position = position_choice()
    tic_tac = replacemnt_choice(tic_tac, position)
    display_game(tic_tac)
    game_on = gameon_choice()


