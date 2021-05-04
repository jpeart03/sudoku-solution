from board import solution_board_2d, starting_board_2d


class Solver:
    def __init__(self, new_puzzle):
        self.game_board = new_puzzle
        # Dictionary to help with box indexes of 2d array:
        # - the key represents the result of idx in question // 3
        # - the values represent the idx that have the same result i.e. the "box"
        # - works for both row and col idx (since they are each 0 - 8)
        self.boxes = {0: [0, 1, 2], 1: [3, 4, 5], 2: [6, 7, 8]}

    def is_row_viable(self, row_idx, num):
        return True if num not in self.game_board[row_idx] else False

    def is_col_viable(self, col_idx, num):
        col_nums = [self.game_board[n][col_idx] for n in range(9)]
        return True if num not in col_nums else False

    def is_box_viable(self, row_idx, col_idx, num):
        box_row_indexes = self.boxes.get(row_idx // 3)
        box_col_indexes = self.boxes.get(col_idx // 3)
        box_nums = [
            self.game_board[r][c] for r in box_row_indexes for c in box_col_indexes
        ]

        return True if num not in box_nums else False


s = Solver(starting_board_2d)
print(s.is_box_viable(1, 1, 1))
