import pprint
from board import solution_board_2d, starting_board_2d


class Solver:
    def __init__(self, new_puzzle):
        self.game_board = new_puzzle.copy()
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

    def is_move_viable(self, row_idx, col_idx, num):
        return (
            self.is_row_viable(row_idx, num)
            and self.is_col_viable(col_idx, num)
            and self.is_box_viable(row_idx, col_idx, num)
        )

    # TODO: pass row num to avoid excessive iterations
    def solve(self):
        # loop through each row
        for row_idx in range(9):
            # loop through each col in that row
            for col_idx in range(9):
                # make sure we're only editing open cells (0's)
                if self.game_board[row_idx][col_idx] == 0:
                    # brute force try possible numbers 1 - 9
                    for num in range(1, 10):
                        # check if move is viable
                        if self.is_move_viable(row_idx, col_idx, num):
                            self.game_board[row_idx][col_idx] = num
                            self.solve()
                            self.game_board[row_idx][
                                col_idx
                            ] = 0  # set after backtracking
                    return  # if we got here no numbers worked, so return backtrack to previous solve call
        pprint.pprint(
            self.game_board
        )  # finished iterating through board. Print completed board


if __name__ == "__main__":
    s = Solver(starting_board_2d)
    s.solve()
