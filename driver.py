from utils import Board


class Driver:
    def __init__(self):
        self.rows = 20
        self.cols = 30
        self.mines = 25

        self.board_initialization()

    def board_initialization(self):
        self.board = Board(r=self.rows, c=self.cols, m=self.mines)

        self.board.init_board()
        self.board.place_mines()
        self.board.eval_nums()

    def get_verify_input(self):

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
        # while True:
        #     pass


if __name__ == '__main__':
    print("*" * 50)
    d = Driver()
    d.main_loop()
