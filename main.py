def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                a = board[i][j]
                if a == 0:
                    print(" ")
                else:
                    print(str(a))
            else:
                a = board[i][j]
                if a == 0:
                    print(" " + " ", end="")
                else:
                    print(str(a) + " ", end="")


def find_empty_field(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


def solve(board):
    empty = find_empty_field(board)
    if empty is None:
        return True
    y, x = empty

    for i in range(1, 10):
        if is_correct(board, i, x, y):
            board[y][x] = i

            if solve(board):
                return True

            board[y][x] = 0

    return False


def is_correct(board, value, x, y):
    # check row:
    for i in range(len(board[0])):
        if board[y][i] == value and i != x:
            return False

    # check column:
    for i in range(len(board)):
        if board[i][x] == value and i != y:
            return False

    # check box (3x3 square):
    y0 = y // 3
    y0 *= 3
    x0 = x // 3
    x0 *= 3
    for i in range(y0, y0 + 3):
        for j in range(x0, x0 + 3):
            if board[i][j] == value and i != y and x != j:
                return False

    return True


def main():
    choice = -1
    while choice != 0:
        print("Enter difficulty: ")
        print("1 - easy")
        print("2 - medium")
        print("3 - hard")
        print("0 - exit")
        choice = int(input("Your choice: "))

        if choice == 1:
            with open('easySudoku.txt', "r") as easy_sudoku_file:
                easy_board = [[int(x) for x in line.split()] for line in easy_sudoku_file]

            print("\nBefore solving: ")
            print_board(easy_board)
            print("\nResolution is in progress...")
            if solve(easy_board) is False:
                print('\n' + "Invalid example, solving the problem is impossible!")
            else:
                print('\n' + "Solved sudoku: ")
                print_board(easy_board)
            print("")

            easy_sudoku_file.close()

        elif choice == 2:
            with open('mediumSudoku.txt', "r") as medium_sudoku_file:
                medium_board = [[int(x) for x in line.split()] for line in medium_sudoku_file]

            print("\nBefore solving: ")
            print_board(medium_board)
            print("\nResolution is in progress...")
            if solve(medium_board) is False:
                print('\n' + "Invalid example, solving the problem is impossible!")
            else:
                print('\n' + "Solved sudoku: ")
                print_board(medium_board)
            print("")

            medium_sudoku_file.close()

        elif choice == 3:
            with open('hardSudoku.txt', "r") as hard_sudoku_file:
                hard_board = [[int(x) for x in line.split()] for line in hard_sudoku_file]

            print("\nBefore solving: ")
            print_board(hard_board)
            print("\nResolution is in progress...")
            if solve(hard_board) is False:
                print('\n' + "Invalid example, solving the problem is impossible!")
            else:
                print('\n' + "Solved sudoku: ")
                print_board(hard_board)
            print("")

        else:
            print('')


if __name__ == '__main__':
    main()

print('Code is done!')
