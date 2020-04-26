board_array = [
    [0, 8, 0, 0, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 0, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 0, 0, 2, 0, 6, 0, 0, 7]
]

# TODO: create GUI


def print_board(board):
    """
    Prints formatted board
    :param board: 2D array
    """
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("=====================")
        for col in range(len(board)):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end=" ")


def find_empty(board):
    """
    Finds next empty space
    :param board: 2D array
    :return: row, col of next empty space or none
    """
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return row, col
    return None


def solve(board):
    """
    Solves board using backtracing
    :param board: 2D array
    :return: True if solved, False if invalid combination
    """
    position = find_empty(board)
    if position is None:
        return True
    x, y = position
    for value in range(1, 10):
        if valid(board, x, y, value):
            board[x][y] = value
            if solve(board):
                return True
            board[x][y] = 0
    return False


def valid(board, x, y, value):
    """
    Determines validity of test number
    :param board: 2D array
    :param x: x coordinate of space
    :param y: y coordinate of space
    :param value: test value
    :return: True if valid placement, False otherwise
    """
    for col_counter in range(len(board)):
        if board[x][col_counter] == value:
            return False

    for row_counter in range(len(board)):
        if board[row_counter][y] == value:
            return False

    box_x = x // 3
    box_y = y // 3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y * 3, box_y*3 + 3):
            if board[i][j] == value:
                return False

    return True


if __name__ == '__main__':
    print_board(board_array)
    print("\n")
    solve(board_array)
    print_board(board_array)