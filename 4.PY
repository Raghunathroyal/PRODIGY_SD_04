def is_valid(board, row, col, num):
    # Check if the number can be placed in the current row
    if num in board[row]:
        return False

    # Check if the number can be placed in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number can be placed in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    # Find an empty location (cell with 0 value)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_location = find_empty_location(board)

    # If there are no empty locations, the puzzle is solved
    if not empty_location:
        return True

    row, col = empty_location

    # Try placing numbers 1 through 9 in the empty location
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num

            # Recursively try to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the number leads to an invalid solution, backtrack
            board[row][col] = 0

    # No number can be placed in the current location
    return False

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents an empty cell)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku Puzzle:")
    print_sudoku(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Puzzle:")
        print_sudoku(sudoku_board)
    else:
        print("\nNo solution exists.")
