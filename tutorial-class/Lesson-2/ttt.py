
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
    input_row = input(f'Player {current_player}, Enter row (e.g. 0,1,2): ')
    input_col = input(f'Player {current_player}, Enter column (e.g. 0,1,2): ')

    board[int(input_row)][int(input_col)] = current_player

    # X <==> ()
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'


