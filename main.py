from pprint import pprint


def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None


def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def solve_sudoku(puzzle):
    # step 1: choose where to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're only allowed valid inputs
    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # step 3: check if its a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then plase that guess on the puzzle:
            puzzle[row][col] = guess
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        # step 5: if not valid OR if our guess does not solve the puzzle,
        # then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE
    return False


if __name__ == '__main__':
    example_board = [
        [-1, -1, 7, 4, -1, -1, 8, -1, -1],
        [-1, -1, 4, -1, -1, 3, 1, -1, -1],
        [-1, -1, -1, -1, 1, -1, 7, -1, 5],

        [-1, 7, 2, -1, -1, -1, -1, -1, -1],
        [8, -1, -1, -1, -1, 9, -1, -1, -1],
        [-1, 4, -1, -1, -1, -1, -1, -1, -1],

        [-1, -1, 5, -1, -1, 2, -1, -1, 8],
        [-1, -1, -1, 1, -1, -1, 4, -1, -1],
        [9, -1, -1, -1, 7, -1, 5, 6, -1]
    ]

    pprint(solve_sudoku(example_board))
    pprint(example_board)
