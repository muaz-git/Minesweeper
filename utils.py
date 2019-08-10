import random

class Cell:
    def __init__(self):
        self.state = False  # if there is a mine in this cell.
        self.clicked = False  # if user have clicked to this cell.
        self.val = -1  # number of cells which contain mine in the neighbourhood.

    def contains_mine(self):
        # tests if this cell contains mine or not, if it does return True else return False.
        self.clicked = True
        return self.state

class Board:
    def __init__(self, r, c, m):
        self.rows = r  # number of rows in the game
        self.cols = c  # number of cols in the game
        self.num_mines = m  # number of mines in the game
        self.cells_dict = {}  # 2d dictionary that contains all cells of the game.

    def init_board(self):
        # initialize the board by creating a 2d dictionary self.cells of dimensions rows and columns.
        # for each element in the dictionary it creates a cell object and assign appropriate values.
        for i in range(self.rows):
            self.cells_dict[i] = {}

            for j in range(self.cols):
                self.cells_dict[i][j] = Cell()


    def place_mines(self):
        # it places self.mines randomly across the whole board and updates the self.cells.
        unique_tuples = []
        while len(unique_tuples) <self.num_mines:
            r_idx = random.randint(0, self.rows-1)
            c_idx = random.randint(0, self.cols-1)
            tpl = (r_idx, c_idx)
            if tpl not in unique_tuples:
                unique_tuples.append(tpl)

                # changing the state that the cell has mine.
                self.cells_dict[r_idx][c_idx].state = True

        print("Bombs are at {}".format(unique_tuples))


    def eval_nums(self):
        # for each cell it calculates the number of bombs in the neighboring cells and updates the self.cells
        for i in range(self.rows):
            for j in range(self.cols):
                pass


    def display_board(self):
        # it displays the whole board to CLI.
        print("Printing Board")

        # for j in range(self.cols):
        #     if j < self.cols - 1:
        #         print(j+1, end="|")
        #     else:
        #         print(j+1)

        for i in range(self.rows):
            for j in range(self.cols):

                val_to_print = "_"
                if self.cells_dict[i][j].clicked:
                    val_to_print = str(self.cells_dict[i][j].val)
                # if self.cells_dict[i][j].state:
                #     val_to_print = '*'
                if j < self.cols-1:
                    print(val_to_print, end ="|")
                else:
                    print(val_to_print)