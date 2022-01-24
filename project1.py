#check if the numbers by the user are correct and between 0-2
def get_user_input(matrics, player_char):
    invalid_input = True
    while invalid_input:
        row_number = input('Please insert a row number: ')
        col_number = input('Please insert a column number: ')
        valid_row_number = row_number.isnumeric() and int(row_number) <= 2 and int(row_number) >= 0
        valid_col_number = col_number.isnumeric() and int(col_number) <= 2 and int(col_number) >= 0
        if valid_row_number and valid_col_number and matrics[int(row_number)][int(col_number)] == '_':
            matrics[int(row_number)][int(col_number)] = player_char
            invalid_input = False
        else:
            print('Invalid input, please insert values again..')
    return row_number,col_number

def is_winner(matrics):
    # Three in a row
    for i in range(3):
        if matrics[i][0] == matrics[i][1] == matrics[i][2] != '_':
            return True
        if matrics[0][i] == matrics[1][i] == matrics[2][i] != '_':
            return True

    # Diagonals
    if matrics[0][0] == matrics[1][1] == matrics[2][2] != '_':
        return True

    if matrics[0][2] == matrics[1][1] == matrics[2][0] != '_':
        return True

    return False

def print_board(matrics):
    for i in range(3):
        print(matrics[i])


def is_tie(matrics):
    for i in range(3):
        for j in range(3):
            if matrics[i][j] == '_':
                return False

    return True

new_game = False
matrics = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
player_char = 'X'

while True:
    if new_game:
        new_game = False
        matrics = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        player_char = 'X'

    row_number, col_number = get_user_input(matrics, player_char)

    print_board(matrics)

    if is_winner(matrics):
        print('We got a winner! the winner is: ' + player_char)
        new_game = True
        continue

    if is_tie(matrics):
        print("Its a tie! Starting a new game..")
        new_game = True
        continue

    if player_char == 'X':
        player_char = 'O'
    else:
        player_char = 'X'

