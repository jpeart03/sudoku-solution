from board import solution_board_2d, starting_board_2d


class Solver:
    def __init__(self, new_puzzle):
        self.game_board = new_puzzle

    def is_row_viable(self, row_idx, num):
        return True if num not in self.game_board[row_idx] else False

    def is_col_viable(self, col_idx, num):
        col_nums = [self.game_board[n][col_idx] for n in range(9)]
        return True if num not in col_nums else False

    def is_box_viable(self, row_idx, col_idx, num):
        pass


s = Solver(starting_board_2d)
print(s.is_row_viable(2, 8))
