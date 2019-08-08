class Cell:
    def __init__(self):
        self.state = None
        self.clicked = None
        self.val = None


class Board:
    def __init__(self):
        self.cells = None  # 2d dictionary that contains all cells of the game.
        self.rows = 20  # number of rows in the game
        self.cols = 30  # number of cols in the game
        self.num_mines = 25  # number of mines in the game
