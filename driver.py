from utils import Board


class Driver:
    def __init__(self, r, c, m):
        self.rows = r
        self.cols = c
        self.mines = m

        self.board_initialization()

    def board_initialization(self):
        # initializes the board, places the mines and pre-evaluate the numbers of neigbouring mines in each cell.
        self.board = Board(r=self.rows, c=self.cols, m=self.mines)

        self.board.init_board()
        self.board.place_mines()
        self.board.eval_nums()
        # self.board.display_board_dbg()

    def get_verify_input(self):
        # Makes sure that input is a valid integer and in the limits.
        while True:
            try:
                r = int(input("Enter row in [1, {}]: ".format(self.rows)))
                c = int(input("Enter column in [1, {}]: ".format(self.cols)))
            except ValueError:
                print("Enter valid input.")
                continue

            if 1 <= r <= self.rows and 1 <= c <= self.cols:
                break
            else:
                print("Enter valid input.")

        # converting inputs to array indices.
        r = r - 1
        c = c - 1

        return r, c

    def main_loop(self):
        print("This Minesweeper has {} rows and {} columns.\n".format(self.rows, self.cols))

        # r, c = self.get_verify_input()
        while True:
            self.board.display_board()
            r, c = self.get_verify_input()
            self.board.handle_clicking(r, c)

            status = self.board.get_game_status()

            if status < 0:
                print("\n\n\t\tGame Over! You Lost!")
                self.board.display_board(over=True)
                break
            if status == 1:
                print("\n\n\t\tCongratulations! You won!")
                self.board.display_board(over=True)
                break

if __name__ == '__main__':
    print("*" * 50)
    d = Driver(r=4, c=4, m=4)
    d.main_loop()
    print("*" * 50)
