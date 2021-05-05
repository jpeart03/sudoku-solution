import pprint

chad_board_2d = [
 [6, 1, 9, 2, 3, 8, 7, 4, 5],
 [2, 7, 4, 5, 6, 1, 3, 9, 8],
 [8, 5, 3, 9, 4, 7, 6, 2, 1],
 [4, 8, 6, 3, 5, 2, 1, 7, 9],
 [7, 9, 2, 6, 1, 4, 5, 8, 3],
 [5, 3, 1, 8, 7, 9, 2, 6, 4],
 [9, 4, 5, 7, 2, 3, 8, 1, 6],
 [3, 2, 8, 1, 9, 6, 4, 5, 7],
 [1, 6, 7, 4, 8, 5, 9, 3, 2]]

starting_board_2d = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution_board_2d = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

# print(solution_board_2d)
# pprint.pprint(solution_board_2d)

class SudokuSolver:
    
    def __init__(self, in_string):
        self.board = self.build_board(in_string)
        self.boxes = {0: [0,1,2], 1: [3,4,5], 2: [6,7,8]}
    
    def build_board(self, in_string):
        # make the board from 81 value incoming string
        test_2d_array = [list(map(int, in_string[i : i + 9])) for i in range(0, 81, 9)]
        return test_2d_array

    def is_row_viable(self, row_i, guess_number):
        # Can I put this guess_number here based on the other values in the row
        return guess_number not in self.board[row_i]

    def is_column_viable(self, column_j, guess_number):
        # Can I put this guess_number here based on the other values in the column
        # self.board is the 2D list; row_i is the row, column_j is the column index
        return guess_number not in [self.board[row_i][column_j] for row_i in range(9)]

    def is_box_viable(self, row_i, column_j, guess_number):
        # Can we add guess_number into this box? Returns True/False 
        box_row_indexes = self.boxes.get(row_i // 3)
        box_col_indexes = self.boxes.get(column_j // 3)
        return guess_number not in [self.board[r][c] for r in box_row_indexes for c in box_col_indexes]

    def is_move_viable(self, row_i, column_j, guess_number):
        # For empty cells: check row, column, box 
        # Return T/F is guess_number viable
        # Run is_row_viable(), is_column_viable(), is_box_viable()
        return self.is_row_viable(row_i, guess_number) and self.is_column_viable(column_j, guess_number) and self.is_box_viable(row_i, column_j, guess_number)

    def solve(self):
        # Loop through each Row
        for row_i in range(9):
            #   Loop through each column
            for column_j in range(9):
            #       Check if cell value == 0
                if self.board[row_i][column_j] == 0:
            #           Loop through 9 guess_number range(1, 10)
                    for guess_number in range(1, 10):
            #               Is the guess_number valid? is_move_viable
                        if self.is_move_viable(row_i, column_j, guess_number):
                            self.board[row_i][column_j] = guess_number
                            self.solve()
                            # Only runs next line if next iteration of solve() never gets into the is_move_viable if block
                            self.board[row_i][column_j] = 0
                    # return runs if for loop fails- we guessed all the numbers and none of them work
                    return
        self.display_board()

    def display_board(self):
        pprint.pprint(self.board)


    
new_board = SudokuSolver("619030040270061008000047621486302079000014580031009060005720806320106057160400030")
new_board.solve()
