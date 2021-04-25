def sudoku_board_print(board):
    # Print row
    for r in range(len(board)):
        if r % 3 == 0 and r != 0 :
            print("- - - - - - - - - - - - - ")

        # Print collum
        for c in range(len(board[0])):
            if c % 3 == 0 and c != 0 :
                print(" | ", end="")

            #The end of the row
            if c == 8:
                print(board[r][c])
            else:
                print(str(board[r][c]) + " ", end = "")


def find_empty_space(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return r,c

    return None


def valid(board, number, position):
    # Check row
    for c in range (len(board[0])):
        if board[position[0]][c] == number and position[1] != c:
            return False

    # Check collum
    for r in range (len(board)):
        if board[r][position[1]] == number and position[0] != r:
            return False

    # Check box
    box_r = (position[0] // 3) * 3  # Start position of row of the box
    box_c = (position[1] // 3) * 3  # Start position of collum of the box

    for r in range(box_r, box_r + 3):
        for c in range (box_c, box_c + 3):
            if board[r][c] == number and (r,c) != position:
                return False

    return True


def solve(board):
    # Find empty space
    find = find_empty_space(board)

    if not find: # not 1 = 0,  not 0 = 1
        return True
    else:
        row, col = find

    # Find right combination of numbers
    for num in range(1,10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):  # backtracking
                return True

            board[row][col] = 0

    return  False


sudoku_board = [
    [0, 0, 2,   0, 0, 0,    5, 0, 4],
    [0, 0, 0,   0, 0, 0,    0, 0, 0],
    [0, 0, 0,   0, 8, 2,    6, 3, 0],

    [0, 0, 0,   3, 9, 0,    7, 0, 6],
    [1, 0, 0,   0, 0, 0,    0, 0, 0],
    [0, 4, 0,   7, 0, 0,    0, 0, 0],

    [0, 7, 8,   5, 0, 0,    0, 0, 0],
    [0, 0, 4,   0, 6, 8,    0, 0, 2],
    [6, 0, 1,   0, 0, 0,    0, 0, 9]
]

print("Initial state:")
sudoku_board_print(sudoku_board)
print("\n")
print("Final state:")
solve(sudoku_board)
sudoku_board_print(sudoku_board)
