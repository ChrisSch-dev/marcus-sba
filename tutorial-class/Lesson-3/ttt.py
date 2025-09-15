from xml.dom.minidom import getDOMImplementation


# def function
def init_board(grid_size):
    board = []
    for j in range(grid_size):
        row = []
        for i in range(grid_size):
            row.append(' ')  # add element to row
        board.append(row)  # add new row to the board
    return board

def check_row(board, grid_size, current_player):
    for j in range (grid_size):
        row = board[j]
        count = 0
        for i in range(grid_size):
            if row[i] == current_player:
                count += 1
            if count == grid_size:
                return True
    return False

def check_col(board, grid_size, current_player):
    for col_index in range(grid_size):
        count = 0
        for row_index in range(grid_size):
            if board[row_index][col_index] == current_player:
                count += 1
            if count == grid_size:
                return True
    return False

def check_d(board, grid_size, current_player):
    count = 0
    for i in range (grid_size):
        if board[i][i] == current_player:
            count += 1
        if count == grid_size:
            return True

    count = 0
    for i in range (grid_size):
        if board[i][grid_size-i-1] == current_player:
            count += 1
        if count == grid_size:
            return True
    return False

def check_draw(board):
    count = 1
    for i in range(0, 3):
        for k in range(0, 3):
            if board[i][k] != " ":
                count += 1

    if count == 10:
        return True
    return False

def print_board(board):
    for i in range (grid_size):
        print(board[i])

# init variable
current_player = 'X'
grid_size = 3
board = init_board(grid_size)

# lib logic
while True:
    print_board(board)

    if check_draw(board):
        print("DRAW")
        exit()


    input_row = input(f'Player {current_player}, Enter row (e.g. 0,1,2): ')
    input_col = input(f'Player {current_player}, Enter column (e.g. 0,1,2): ')

    if input_row not in ["0", "1", "2"] or input_col not in ["0", "1", "2"]:
        print("Your input is invalid")

    board[int(input_row)][int(input_col)] = current_player

    if (check_col(board, grid_size, current_player) or check_row(board, grid_size, current_player) or check_d(board, grid_size, current_player)):
        print(current_player, "WIN")
        print_board(board)


        exit()

    # X <==> ()
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'

