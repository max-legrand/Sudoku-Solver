import random
from text_solver import valid


def make_board(m=3):
    """
    generates board
    :param m: size of row
    :return: final board
    """
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        """
        Search for solution starting at position C
        :param c: starting position for solution search
        :return: board if solution generated, none otherwise
        """
        i = c // n
        j = c % n
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if valid(board, i, j, x):
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            board[i][j] = None
            return None

    return search()


class Grid:
    """
    Grid class representing a board
    """
    def __init__(self, board, rows, cols):
        """
        initialize grid
        :param board: 2D array
        :param rows: #rows
        :param cols: #cols
        """
        self.board = board
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j) for j in range(cols)] for i in range(rows)]
        self.model = None
        self.selected = None

    def select(self, row, col):
        """
        Set selected square
        :param row: row of cube
        :param col: col of cube
        """
        for row_count in range(self.rows):
            for col_count in range(self.cols):
                self.cubes[row_count][col_count].selected = False
        self.cubes[row][col].selected = True
        self.selected = (row, col)


class Cube:
    """
    Class representing individual square on board
    """
    def __init__(self, value, row, col):
        """
        intialize cube
        :param value: value of cube
        :param row: row location
        :param col: column location
        """
        self.value = value
        self.row = row
        self.col = col
        self.selected = False
        self.temp = 0
