class Cell:
    def __init__(self):
        self.state = False  # if there is a mine in this cell.
        self.clicked = False  # if user have clicked to this cell.
        self.val = 0  # number of cells which contain mine in the neighbourhood.

    def contains_mine(self):
        # tests if this cell contains mine or not, if it does return True else return False.
        self.clicked = True
        return self.state


class Board:
    def __init__(self):
        self.rows = 20  # number of rows in the game
        self.cols = 30  # number of cols in the game
        self.num_mines = 25  # number of mines in the game
        self.cells = None  # 2d dictionary that contains all cells of the game.

    def init_board(self):
        # initialize the board by creating a 2d dictionary self.cells of dimensions rows and columns.
        # for each element in the dictionary it creates a cell object and assign appropriate values.
        pass

    def place_mines(self):
        # it places self.mines randomly across the whole board and updates the self.cells.
        pass

    def eval_nums(self):
        # for each cell it calculates the number of bombs in the neighboring cells and updates the self.cells
        pass

    def display_board(self):
        # it displays the whole board to CLI.
        pass
