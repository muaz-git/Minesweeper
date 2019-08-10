import random


class Cell:
    def __init__(self):
        self.state = False  # if there is a mine in this cell.
        self.clicked = False  # if user have clicked to this cell.
        self.val = 9  # number of cells which contain mine in the neighbourhood.

    def get_state(self):
        # tests if this cell contains mine or not, if it does return True else return False.
        return self.state

    def set_state(self, v):
        self.state = v

    def get_clicked(self):
        return self.clicked

    def set_clicked(self, v):
        self.clicked = v

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
        while len(unique_tuples) < self.num_mines:
            r_idx = random.randint(0, self.rows - 1)
            c_idx = random.randint(0, self.cols - 1)
            tpl = (r_idx, c_idx)
            if tpl not in unique_tuples:
                unique_tuples.append(tpl)

                # changing the state that the cell has mine.
                self.cells_dict[r_idx][c_idx].set_state(v=True)

        # print("Bombs are at {}".format(unique_tuples))

    def count_bombs_in_nbr(self, r, c):
        # iterates through all the neighbours and counts if there is a bomb in them.
        total_bombs = 0
        nbr = [-1, 0, 1]
        for nr in nbr:
            for nc in nbr:
                nbr_row = r + nr
                nbr_col = c + nc

                if 0 <= nbr_row < self.rows and 0 <= nbr_col < self.cols:
                    if self.cells_dict[nbr_row][nbr_col].get_state():
                        total_bombs += 1

        return total_bombs

    def eval_nums(self):

        # for each cell it calculates the number of bombs in the neighboring cells and updates the self.cells
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.cells_dict[i][j].get_state():
                    total_bombs = self.count_bombs_in_nbr(i, j)
                    self.cells_dict[i][j].val = total_bombs

    def display_board_dbg(self):
        # it displays the whole board to CLI.

        # for j in range(self.cols):
        #     if j < self.cols - 1:
        #         print(j+1, end="|")
        #     else:
        #         print(j+1)

        for i in range(self.rows):
            for j in range(self.cols):

                # val_to_print = "_"
                # if self.cells_dict[i][j].clicked:
                val_to_print = str(self.cells_dict[i][j].val)
                if self.cells_dict[i][j].get_state():
                    val_to_print = '*'
                if j < self.cols - 1:
                    print(val_to_print, end="|")
                else:
                    print(val_to_print)

    def display_board(self, over=False):
        # it displays the whole board to CLI.
        print()
        print(str('   ').rjust(2, ' '), end=" ")
        for j in range(self.cols):

            toprint = str(j+1).rjust(2,' ')
            if j < self.cols - 1:
                print(toprint, end="|")
            else:
                print(toprint)
        print()
        for i in range(self.rows):
            print(str(i+1).rjust(2,' '), end="> ")

            for j in range(self.cols):

                val_to_print = "__"
                if self.cells_dict[i][j].get_clicked() or over:
                    val_to_print = str(self.cells_dict[i][j].val)
                    if self.cells_dict[i][j].get_state():
                        val_to_print = 'XX'

                toprint = str(val_to_print).rjust(2, ' ')

                if j < self.cols - 1:
                    print(toprint, end="|")
                else:
                    print(toprint)

    def handle_clicking(self, r, c):
        # if self.cells_dict[r][c].get_clicked():
        #     # already clicked so do nothing
        #     pass
        # elif self.cells_dict[r][c].get_state():
        #     # cell contains mine so game over.
        #     return -1
        # else:
            # open the cell
            self.cells_dict[r][c].set_clicked(v = True)
            # return 0

    def get_game_status(self):
        # -1 over and failed
        # 0 no status, game should continue
        # 1 user won the game
        flag = False # True if non-mined cell is un-clicked
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells_dict[i][j].get_state() and self.cells_dict[i][j].get_clicked():
                    return -1

                if (not self.cells_dict[i][j].get_state()) and (not self.cells_dict[i][j].get_clicked()):
                    # cell does not have mine and not clicked as well, should be continued
                    flag = True

            # if flag:
            #     break

        if flag:
            return 0
        else:
            # if cell with mine is not clicked and all other cells are opened then return game win signal
            return 1

